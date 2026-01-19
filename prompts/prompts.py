IDEA_ANALYSIS_PROMPT = """
You are an experienced startup co-founder and investor with deep expertise in evaluating startup feasibility.

STEP 1: FEASIBILITY ANALYSIS

Analyze the following startup idea for feasibility. Be direct, structured, and provide specific reasoning.

Evaluate these dimensions:
1. **Technical Complexity**: What technology stack is required? How hard to build? Rate: Low/Medium/High
2. **Time to MVP**: How many weeks to build a working prototype? Be realistic.
3. **Cost Requirements**: Estimate budget needed (server costs, tools, hiring). Include rough numbers.
4. **Team Effort**: How many developers/founders needed? Full-time or part-time?
5. **Dependency Analysis**: What external services or integrations are critical?
6. **Feasibility Verdict**: Is this feasible or not? Explain clearly why or why not.

Format your response as:
- Technical Complexity: [Level] - [Brief explanation]
- Estimated Time to MVP: [X weeks]
- Budget Estimate: $[X] for [what]
- Team Size: [X developers, X designers, X founders]
- Critical Dependencies: [List key dependencies]
- Feasibility Verdict: [YES/NO] - [Clear reasoning]

Startup Idea:
{idea}
"""

MARKET_ANALYSIS_PROMPT = """
You are a market researcher and investor with expertise in identifying target markets and competitive landscapes.

STEP 2: MARKET ANALYSIS

Analyze the market opportunity for this startup idea.

Evaluate these dimensions:
1. **Target Users**: Who exactly uses this? (Demographics, psychographics, job titles, pain points)
2. **Market Size**: Estimate total addressable market (TAM) - is it large enough?
3. **Market Demand**: Why do users need this RIGHT NOW? What's the urgency?
4. **Competition**: Who are 2-3 direct competitors? How is this idea different?
5. **Differentiation**: What's the unique value proposition? Why choose this over alternatives?
6. **Go-to-Market**: How will you reach first customers? (Distribution channels)

Format your response as:
- Target Users: [Description]
- Market Size: $[X] TAM (or X potential users)
- Demand Signal: [Why is demand high?]
- Top 3 Competitors: [Names and brief comparison]
- Unique Value Proposition: [Clear, one-sentence differentiator]
- Initial Go-to-Market: [Specific channels to reach users]

Startup Idea:
{idea}
"""

RISK_ANALYSIS_PROMPT = """
You are a startup risk analyst with experience identifying and mitigating startup failure modes.

STEP 3: RISK IDENTIFICATION

Identify all major risks that could derail this startup.

Analyze these risk categories:
1. **Technical Risks**: What could go wrong with the product? (Scalability, security, integrations)
2. **Market Risks**: What if demand doesn't materialize? Competitive response? Market timing?
3. **Execution Risks**: Can the team execute? Key person dependencies? Timeline slippage?
4. **Financial Risks**: Runway concerns? Unit economics unclear? Funding challenges?
5. **Regulatory/Legal Risks**: Are there compliance issues? (Privacy, licensing, contracts)

For each risk:
- Rate severity: High/Medium/Low
- Describe impact
- Suggest mitigation strategy

Format your response as:
**TECHNICAL RISKS:**
- [Risk name] (Severity: High/Medium/Low) - [Impact] - [Mitigation]

**MARKET RISKS:**
- [Risk name] (Severity: High/Medium/Low) - [Impact] - [Mitigation]

**EXECUTION RISKS:**
- [Risk name] (Severity: High/Medium/Low) - [Impact] - [Mitigation]

**FINANCIAL RISKS:**
- [Risk name] (Severity: High/Medium/Low) - [Impact] - [Mitigation]

**REGULATORY/LEGAL RISKS:**
- [Risk name] (Severity: High/Medium/Low) - [Impact] - [Mitigation]

Startup Idea:
{idea}
"""

FEATURE_PROMPT = """
You are a product strategist with expertise in designing lean, high-impact MVPs.

STEP 4: IDEA IMPROVEMENT & MVP FEATURE DEFINITION

Review this startup idea and suggest improvements. Then define the MVP.

Part 1: IDEA IMPROVEMENT
- What features should be REMOVED because they're not essential?
- What scope should be REDUCED to focus on the core problem?
- How can you simplify without losing value?
- What's the strongest, most differentiated version of this idea?

Part 2: MVP FEATURE LIST
Define ONLY the essential features needed to validate the core hypothesis.

Format your response as:

**IDEA IMPROVEMENTS:**
- [What to remove/change and why]

**CORE HYPOTHESIS:**
[One clear statement of what you're testing - e.g., "Users will pay for automated X if it saves them Y hours"]

**MVP FEATURES (Maximum 5):**
1. [Feature Name] - [Why essential] - [Expected user outcome]
2. [Feature Name] - [Why essential] - [Expected user outcome]
3. [Feature Name] - [Why essential] - [Expected user outcome]
4. [Feature Name] - [Why essential] - [Expected user outcome]
5. [Feature Name] - [Why essential] - [Expected user outcome]

**OUT OF SCOPE FOR MVP:**
- [Non-essential feature]
- [Non-essential feature]
- [Non-essential feature]

Startup Idea:
{idea}
"""

MVP_PROMPT = """
You are an experienced product manager and startup executor.

STEP 5: MVP PLANNING - PHASED ROADMAP

Create a detailed MVP roadmap broken into phases. Each phase should be completable in 2-4 weeks.

Requirements:
- Each phase should have clear deliverables
- Phases build toward a launchable MVP
- Identify what gets built in each phase
- Identify dependencies between phases
- Note key milestones (alpha, beta, launch)

Format your response as:

**PHASE 1: [Name] (Weeks 1-3)**
- Build: [List specific features/components]
- Key Deliverable: [What's complete at end of phase?]
- Success Criteria: [How do you know it works?]

**PHASE 2: [Name] (Weeks 4-6)**
- Build: [List specific features/components]
- Key Deliverable: [What's complete at end of phase?]
- Success Criteria: [How do you know it works?]

**PHASE 3: [Name] (Weeks 7-9)**
- Build: [List specific features/components]
- Key Deliverable: [What's complete at end of phase?]
- Success Criteria: [How do you know it works?]

**PHASE 4: LAUNCH & VALIDATION (Weeks 10+)**
- Action: [Beta launch, get first users, measure]
- Success Criteria: [X users, X signups, positive feedback]

**KEY DEPENDENCIES:**
- [Dependency that must be completed first]
- [Dependency that blocks other phases]

Startup Idea:
{idea}
"""

TIMELINE_PROMPT = """
You are a startup execution expert with experience shipping products under time pressure.

STEP 6: EXECUTION TIMELINE

Create a detailed, week-by-week execution timeline for the first 12 weeks.

Requirements:
- Be specific about WHAT gets done each week
- Include team activities (hiring, partnerships, user research)
- Include business activities (fundraising, marketing prep)
- Mark key milestones clearly
- Be realistic about what a small team can do

Format your response as:

**WEEK 1-2: Foundation**
- [Specific task] - Owner: [role]
- [Specific task] - Owner: [role]
- Milestone: [What's complete?]

**WEEK 3-4: Core Development**
- [Specific task] - Owner: [role]
- [Specific task] - Owner: [role]
- Milestone: [What's complete?]

**WEEK 5-6: Feature Completion**
- [Specific task] - Owner: [role]
- [Specific task] - Owner: [role]
- Milestone: [What's complete?]

**WEEK 7-8: Polish & Testing**
- [Specific task] - Owner: [role]
- [Specific task] - Owner: [role]
- Milestone: [What's complete?]

**WEEK 9-10: Beta Launch Prep**
- [Specific task] - Owner: [role]
- [Specific task] - Owner: [role]
- Milestone: [What's complete?]

**WEEK 11-12: Launch & Iterate**
- [Specific task] - Owner: [role]
- [Specific task] - Owner: [role]
- Milestone: [What's complete?]

**CRITICAL PATH:**
- [Task that cannot be delayed]
- [Task that blocks other tasks]

**ASSUMPTIONS:**
- Team size: [X people]
- Available resources: [funding, tools, partnerships]

Startup Idea:
{idea}
"""
