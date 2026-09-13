# System Design Cheatsheet — for TPM and senior PM-T rounds

Condensed from the classic material (system-design-primer, Designing Data-Intensive Applications, Alex Xu). Enough to design and defend a system in 45 minutes. For deeper study: https://github.com/donnemartin/system-design-primer

---

## Numbers to know

| Thing | Value |
|---|---|
| L1 cache / RAM reference | ~1 ns / ~100 ns |
| SSD random read | ~100 µs |
| HDD seek | ~10 ms |
| Same datacenter round trip | ~0.5 ms |
| Cross-continent round trip | ~150 ms |
| Read 1 MB from SSD / network (1 Gbps) | ~1 ms / ~10 ms |
| One server (commodity) | ~10k–50k simple QPS; ~1k–5k with DB writes |
| MySQL single node | ~5k–20k QPS; ~1–2 TB comfortable |
| Redis single node | ~100k+ QPS; RAM-bound |
| Kafka partition | ~10s of MB/s |
| Availability: 99.9% / 99.99% | 8.7 h / 52 min downtime per year |
| 1 day | ~86,400 s ≈ 10^5 s (use for QPS math) |
| Char / int / UUID | 1 B / 4 B / 16 B; a tweet ~300 B; a photo ~200 KB–2 MB; a minute of 1080p video ~50–100 MB |

Estimation pattern: DAU × actions/user/day ÷ 10^5 = avg QPS; peak = 2–5× avg. Storage = writes/day × size × retention.

---

## Building blocks — what they are and when to use

**Load balancer** — spreads traffic; L4 (TCP) vs L7 (HTTP, can route by path/header). Health checks, sticky sessions (avoid), enables horizontal scaling. Use always at the edge.

**API gateway** — auth, rate limiting, routing, request logging in one place.

**CDN** — caches static/media content at edge PoPs near users. Push vs pull. Use for images, video, JS/CSS. Reduces origin load and latency.

**Cache (Redis/Memcached)** — in-memory KV. Patterns: cache-aside (app reads cache, on miss reads DB and populates), write-through, write-behind. Eviction: LRU/LFU/TTL. Problems: stale data, thundering herd (use locks/jitter), hot keys (replicate/shard key). Use when read-heavy with repeat access.

**Relational DB (Postgres/MySQL)** — ACID, joins, strong consistency, good for transactions (payments, inventory). Scale via read replicas → vertical → sharding (painful). Indexes: B-tree; add on query columns; each index costs write speed.

**NoSQL** —
- *Key-value* (DynamoDB, Redis): simple lookups, massive scale.
- *Wide-column* (Cassandra, Bigtable): write-heavy, time-series, tunable consistency, no joins.
- *Document* (MongoDB): flexible schema, nested docs.
- *Graph* (Neo4j): relationship traversal.
Choose NoSQL for scale + simple access patterns; relational for complex queries/transactions.

**Blob/object storage (S3/GCS)** — media, files, backups. Cheap, durable, not for low-latency small reads (put a CDN in front).

**Message queue / log (Kafka, SQS, RabbitMQ)** — decouple producers and consumers, absorb bursts, async processing, fan-out to multiple consumers, replay (Kafka). Semantics: at-least-once (dedupe with idempotency keys) is the practical default; exactly-once is expensive.

**Search index (Elasticsearch)** — full-text, fuzzy, faceted search. Built from a change stream off the primary DB.

**Stream processing (Flink, Spark Streaming)** — windowed aggregations (counts per minute), real-time features.

**Batch (Spark, Hadoop)** — daily aggregates, ML training, reports.

**Coordination (ZooKeeper/etcd)** — leader election, config, distributed locks.

**Service mesh / RPC (gRPC)** — internal service-to-service; retries, timeouts, circuit breakers.

---

## Scaling patterns

- **Horizontal scaling** — stateless services behind an LB; state moves to DB/cache.
- **Replication** — leader–follower (writes to leader, reads from followers; replication lag → eventual consistency for reads); multi-leader (conflicts); leaderless (quorum R + W > N).
- **Sharding / partitioning** — by hash of key (even spread, no range queries), by range (range queries, hot spots), by geography. Pick the shard key by the dominant access pattern. Resharding is hard: use consistent hashing.
- **Caching layers** — browser → CDN → gateway → app cache → DB cache.
- **Async everything non-critical** — put it on a queue.
- **Read/write separation (CQRS)** — different models for reads and writes when ratios are extreme.
- **Denormalization / precomputation** — feeds, timelines, counters.

---

## Reliability patterns

- **Redundancy** — no single point of failure; N+1; multi-AZ; multi-region for DR (active-passive or active-active).
- **Timeouts, retries with exponential backoff + jitter, circuit breakers, bulkheads.**
- **Idempotency keys** for any write that may be retried (payments!).
- **Rate limiting** — token bucket / sliding window; per user/IP/API key; at the gateway; return 429.
- **Backpressure** — bounded queues, load shedding, priority.
- **Graceful degradation** — serve stale cache, drop non-essential features.
- **Health checks, monitoring (RED: rate, errors, duration; USE: utilization, saturation, errors), alerting on SLOs, distributed tracing, runbooks.**
- **Deploys** — canary, blue/green, feature flags, rollback plan.

---

## Consistency & CAP in one paragraph

Under a network partition you choose availability (serve possibly stale data) or consistency (refuse/wait). Most consumer features (feeds, likes, views) choose availability + eventual consistency. Money, inventory, auth choose consistency. Say which you pick and why. Related: strong vs eventual vs read-your-own-writes consistency; linearizability; quorum reads.

---

## Worked skeletons for the most common prompts

**URL shortener** — POST /shorten, GET /{code}. Read-heavy (100:1). Code = base62 of a unique ID (ID generator: DB auto-increment, Snowflake, or pre-generated key range) — not a hash (collisions). KV store keyed by code; heavy cache (hot links); 301 vs 302 (302 keeps analytics); analytics via async queue; expiry via TTL.

**News feed** — Post write → store post → fan-out. *Fan-out on write* (push to each follower's feed cache; fast reads, expensive for celebrities) vs *fan-out on read* (pull from followees at read time; cheap writes, slow reads). Hybrid: push for normal users, pull for celebrities (>N followers). Feed cache = per-user list of post IDs in Redis; hydrate posts from post cache/DB; ranking service scores candidates. Media on blob + CDN.

**Chat / messaging** — WebSocket long-lived connections to chat servers; presence service; message stored in wide-column DB keyed by (conversation_id, timestamp); message ID for ordering; delivery receipts; push notifications via APNs/FCM when offline; group chat = fan-out to members; end-to-end encryption means server stores ciphertext only.

**Notification service** — Producers → notification API → queue per channel (push/email/SMS/in-app) → workers → third-party providers. User preferences + rate limiting/dedup + template service; retry with backoff; track delivery status; priority lanes.

**Rate limiter** — At gateway. Token bucket per key in Redis (atomic INCR + TTL or Lua script). Distributed: shared Redis cluster, accept slight over-admission; sliding window log for precision. Return 429 + Retry-After.

**Ride dispatch (Uber)** — Driver location updates (every few seconds) → geo index (geohash / S2 / quadtree) in memory; rider request → find nearby drivers → matching service (ETA-based, not distance) → offer → accept; trip service; pricing (surge) from supply/demand per cell; Kafka for location stream; strong consistency on trip state, eventual on location.

**File sync (Dropbox)** — Client chunks files (4 MB), hashes chunks, uploads only changed chunks to blob storage; metadata DB (file tree, versions, chunk lists); notification service (long-poll/WebSocket) tells other clients about changes; conflict → create "conflicted copy"; dedup via chunk hash.

**Video upload/streaming (YouTube)** — Upload to blob → queue → transcoding pipeline (DAG: split, encode to multiple resolutions/codecs, thumbnails, DRM) → store variants → CDN; adaptive bitrate streaming (HLS/DASH manifests); metadata DB; view counting via stream aggregation; pre-position popular content at edge.

**Typeahead / autocomplete** — Trie (or prefix table) of top-k completions per prefix, built offline from query logs (batch), served from memory with sharding by prefix; client debounce; cache at CDN/browser; personalization layer optional.

**Ad click aggregator** — Click events → Kafka → stream processor (Flink) windowed counts per ad per minute → OLAP store (Druid/ClickHouse); exactly-once via idempotent writes + checkpoints; reconciliation batch job for correctness; late-event handling with watermarks.

**Payments** — API with idempotency key → payment service writes ledger (double-entry, append-only, strongly consistent SQL) → PSP call (Stripe/bank) → webhook/poll for result → state machine (pending → succeeded/failed) → reconciliation job vs PSP reports; retries safe via idempotency; never store PANs (tokenize); audit log.

---

## Phrases that signal seniority

- "The dominant access pattern is X, so I'll shard on Y."
- "This is read-heavy at 100:1, so I'll cache aggressively and accept eventual consistency."
- "Fan-out on write for most users; pull for the top 0.1% with huge followings."
- "Every write here is retried, so it needs an idempotency key."
- "At 10× I'd expect the bottleneck to move from the DB to the fan-out workers."
- "I'd ship the MVP without the ranking service and add it once we have engagement data."
- "The SLO is p99 < 200 ms; we alert on error budget burn, not on individual errors."
