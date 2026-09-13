# Question Bank — by round type and company

Pick questions the candidate hasn't seen (check `~/.claude/interview-coach/log.md`). Rotate companies and difficulty. Vary the surface (consumer, B2B, hardware, infra, AI) so the candidate can't pattern-match.

---

## Product Sense / Design

**Design X (0→1)**
- Design a product to help people find parking in a dense city. (Google)
- Design an alarm clock for the blind. (Google)
- Design a fridge for a family of 5 with two kids under 6. (Google)
- Design a way for Facebook Marketplace to handle high-value items ($5k+). (Meta)
- Design a product for people who just moved to a new city. (Meta)
- Design a mentorship product for Instagram creators. (Meta)
- Design a grocery-delivery experience for elderly users. (Amazon)
- Design Alexa for hotels. (Amazon)
- Design a feature for Apple Watch to help people with anxiety. (Apple)
- Design a "watch with friends" feature for Netflix. (Netflix)
- Design a jobs product for LinkedIn users in the trades (electricians, plumbers).
- Design a product that uses generative AI to help small businesses reply to reviews.
- Design an in-car experience for a 6-hour road trip with kids.
- Design a bookshelf for children. (classic)
- Design a vending machine for blind users. (classic)

**Improve X**
- How would you improve Google Maps for tourists?
- How would you improve YouTube for creators under 1k subscribers?
- Improve Instagram Reels for users over 50.
- Improve Amazon returns.
- Improve Facebook Groups for admins.
- Improve WhatsApp for small businesses in India.
- Improve Netflix's "continue watching" row.
- Improve the Apple App Store search.
- Improve Gmail for people who get 300+ emails/day.
- Improve LinkedIn's feed.
- Improve Uber for drivers.
- Improve Spotify for podcast listeners.

**Favorite / critique**
- What's your favorite product and how would you make it better?
- What's a product you think is poorly designed and why?
- Critique the onboarding of [app the candidate uses].
- What's a product that failed and why?
- What would you change about the Kindle?
- Compare Instagram Stories and Snapchat Stories — who does it better and why?

**Meta-style "people & problems"**
- What problem would you solve for teenagers on Instagram?
- Facebook wants to help people find local events. What would you build?
- How would you make Messenger more useful for families?
- What's the biggest unmet need for small-business owners on Facebook?

---

## Product Strategy

- Should Google build a bank?
- Should Amazon enter the healthcare-provider business? (Amazon)
- Should Netflix launch a live sports product? How?
- Should Meta build its own smartphone?
- How should YouTube respond to TikTok's growth in short video?
- How would you monetize Google Maps further?
- How would you monetize WhatsApp without ads?
- You're CEO of Uber. What are your top 3 priorities?
- Apple is launching a search engine. Good idea? How would you do it?
- How should Amazon think about competing with Shopify?
- Should Netflix add a free ad-supported tier in India?
- What should Google do about generative AI cannibalizing search?
- Which company should acquire Peloton and why?
- Should Meta charge for a verified badge? (retrospective — what would you have decided?)
- How would you grow Threads to 1B users?
- A competitor cut price by 30%. What do you do?

---

## Analytical / Execution / Metrics

**Define metrics**
- How would you measure success for Instagram Reels?
- What metrics would you track for Facebook Marketplace?
- Define success metrics for YouTube Shorts.
- Define success for Amazon Prime Video's ad tier.
- What is the north star metric for Google Maps? Netflix? Uber Eats? Slack?
- How would you measure the success of a new "close friends" feature?
- Define metrics for an internal developer platform (TPM/B2B variant).

**Metric moved — diagnose**
- Instagram Stories posts are down 10% week over week. What do you do?
- Google Search queries are down 5% in Japan. Investigate.
- YouTube watch time is up 15% but revenue is flat. Why?
- Uber ride cancellations increased 20% in NYC. Diagnose.
- Amazon cart-abandonment rate rose from 60% to 70%. What happened?
- Netflix sign-ups are flat but churn dropped. What's going on?
- Messenger DAU is flat but messages sent is up 30%. Interpret.
- App Store rating dropped from 4.6 to 4.1 in two weeks.
- Facebook Marketplace listings went up 40% but transactions are flat.

**Ship or not / tradeoffs**
- An experiment raises time-spent 4% but reduces ad revenue 2%. Ship?
- A change increases sign-ups 8% but 7-day retention drops 3%. Ship?
- Notifications experiment: +6% DAU, +15% notification opt-outs. Ship?
- We can either fix the top 3 bugs or launch feature X this quarter. How do you decide?
- Engineering says the new feed ranking model is 2% better on engagement but 3× the serving cost. What do you do?

**Experiment design**
- Design an A/B test for a new Reels ranking model.
- How would you test whether removing "likes" counts improves wellbeing?
- How would you measure the impact of a new Prime shipping speed on purchase frequency?
- A feature has strong network effects. How do you experiment?

---

## Estimation

- How many Google searches happen per second?
- How many YouTube videos are uploaded per day?
- Estimate the revenue of Uber Eats in London.
- How many Amazon packages are delivered in the US on a typical day?
- How much storage does Gmail need per year?
- Estimate the number of Netflix hours watched per day globally.
- How many photos are uploaded to Instagram per day?
- How much would it cost to run Google Maps' servers for a day?
- How many people are in the air over the US right now?
- Estimate the market size for a dog-walking app in the US.
- How many elevator rides happen in Manhattan per day?

---

## Technical (PM / PM-T)

- Explain what happens when you type google.com and hit enter.
- How does a push notification reach my phone?
- How does Google Search work, at a high level?
- How do recommendation systems work? What data do they need?
- Explain how OAuth "Sign in with Google" works.
- What is an API? Design an API for a weather service.
- Design an API for Instagram's "like" feature. What about rate limiting?
- SQL vs NoSQL — how do you choose?
- What's a CDN and when would you use one?
- What's the difference between latency and throughput? Give a product example of each.
- How would you explain machine learning to a marketing VP?
- What would you ask engineers before believing a 6-month estimate?
- Engineering wants to rewrite the app from scratch. How do you evaluate?
- What's technical debt and how do you prioritize paying it down?
- How does end-to-end encryption work in WhatsApp, and what does it mean for product features?
- What's an LLM, and where would you and wouldn't you use one in [product]?

---

## System Design (TPM / senior PM-T)

- Design a URL shortener (bit.ly).
- Design Instagram's news feed.
- Design WhatsApp / Messenger.
- Design a notification service for Facebook (push, email, in-app).
- Design a rate limiter.
- Design Uber's ride matching / dispatch.
- Design Dropbox / Google Drive file sync.
- Design YouTube's video upload and streaming pipeline.
- Design Google search autocomplete / typeahead.
- Design an ad-click aggregation system (counts per ad per minute).
- Design Amazon's shopping cart & checkout (consistency!).
- Design a payment system / ledger.
- Design a distributed cache (Memcached).
- Design a metrics/monitoring pipeline (like Datadog).
- Design Netflix's content delivery (CDN, encoding, pre-positioning).
- Design a leaderboard for a game with 100M players.
- Design a system to detect duplicate images at Meta scale.
- Design a feature-flag / experimentation platform.
- Design Alexa's voice request pipeline end-to-end.

---

## Program Execution (TPM)

- You're the TPM for launching a new payments feature across 6 teams in 3 countries by Q4. Walk me through how you'd run it.
- Your program is 3 months behind. What do you do?
- Two engineering teams disagree on who owns a critical service. How do you resolve it?
- A dependency team just told you they can't deliver on time. What now?
- How do you build a plan when requirements are still changing?
- You've been given an ambiguous mandate: "make our mobile app faster." Turn it into a program.
- How do you decide what to cut when you have to ship in 6 weeks?
- Design a migration of a monolith to services with zero downtime — as a program, not an architecture.
- How would you run an org-wide reliability (SLO) program?
- Describe how you'd run a launch that needs legal, privacy, security, and 4 eng teams.
- What does your weekly status report look like? Who reads it?
- How do you handle a senior engineer who won't give estimates?
- Post-launch, a Sev-1 incident happens. Walk me through the first 60 minutes and the next 2 weeks.
- How do you decide between adding people and cutting scope?
- How do you track a program with 40 dependencies without drowning in spreadsheets?

---

## Behavioral — by principle / signal

**Ownership / Deliver Results / Drive**
- Tell me about your most significant accomplishment.
- Tell me about a time you took on something outside your job.
- Tell me about a time you delivered under an aggressive deadline.
- Tell me about a project that failed. What did you do?

**Customer Obsession / User empathy**
- Tell me about a time a customer insight changed your direction.
- Tell me about a time you pushed back on leadership for the customer.

**Dive Deep / Analytical**
- Tell me about a time you found something in the data nobody else had.
- Tell me about a decision you made with incomplete data.

**Disagree & Commit / Backbone / Conflict**
- Tell me about a time you disagreed with your manager. What happened?
- Tell me about a time you had to commit to a decision you disagreed with.
- Tell me about a conflict with an engineer/designer. How did you resolve it?
- Tell me about a time you had to say no to a senior stakeholder.

**Influence / Collaboration / Leadership**
- Tell me about a time you influenced a team you had no authority over.
- Tell me about a time you led through ambiguity.
- Tell me about a time you had to align multiple teams with conflicting priorities.

**Earn Trust / Failure / Growth**
- Tell me about a time you made a mistake. How did you handle it?
- Tell me about feedback you received that was hard to hear.
- What would your last manager say you need to improve?

**Invent & Simplify / Think Big / Bias for Action**
- Tell me about a time you simplified a process.
- Tell me about a time you proposed something bold. What happened?
- Tell me about a time you moved fast and it was the right (or wrong) call.

**Hire & Develop / Highest Standards**
- Tell me about a time you coached someone.
- Tell me about a time you refused to ship something because it wasn't good enough.

**Company-specific**
- Why Amazon / Meta / Google / Apple / Netflix? Why this team?
- (Netflix) Tell me about a time you farmed for dissent. / Where do you disagree with our culture memo?
- (Apple) What's a detail in one of our products you'd fix? Why hasn't it been fixed?
- (Google) Tell me about a time you had to make a decision when the right answer wasn't clear.
- (Meta) Tell me about a time you moved fast and broke something. What did you learn?

**Standard follow-up probes (use liberally in mocks):**
- What was the metric before and after?
- What did *you* specifically do, versus the team?
- What would you do differently?
- Who disagreed with you, and what did they say?
- How did you know it worked?
- What was the hardest part?
- Give me another example.
