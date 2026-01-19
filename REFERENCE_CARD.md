# Agent Reference Card

Quick reference for using the Autonomous Startup Validator Agent.

## Command Reference

### Run Main Agent
```bash
python main.py
```
Input: Startup idea (detailed description)
Output: 6-step analysis report
Time: 30-60 seconds

### Run Example Analyses
```bash
python example_usage.py
```
Shows 3 pre-built examples with full analysis

### View Saved Reports
```python
from utils import list_saved_reports
list_saved_reports()
```

### Load Previous Analysis
```python
from utils import load_analysis_report
report = load_analysis_report("analysis_20260118_120000.json")
```

### Compare Two Ideas
```python
from utils import compare_ideas
comparison = compare_ideas(report1, report2)
```

---

## Prompt Descriptions (What Each Step Does)

### STEP 1: IDEA_ANALYSIS_PROMPT
Feasibility Assessment
- Technical complexity (Low/Medium/High)
- Time estimate to MVP (weeks)
- Budget breakdown
- Team size needed
- Verdict: Feasible? YES/NO

### STEP 2: MARKET_ANALYSIS_PROMPT
Market Opportunity
- Target user profiles
- Market size (TAM)
- Demand validation
- Competitor analysis
- Differentiation strategy

### STEP 3: RISK_ANALYSIS_PROMPT
Risk Identification
- Technical risks (severity rated)
- Market risks (severity rated)
- Execution risks (severity rated)
- Financial risks
- Regulatory risks
- Each with mitigation strategy

### STEP 4: FEATURE_PROMPT
MVP Definition
- Scope improvements/removals
- Core hypothesis statement
- 3-5 MVP features ONLY
- Out-of-scope list
- Why each feature matters

### STEP 5: MVP_PROMPT
Phased Roadmap
- 3-4 development phases
- Deliverables per phase
- Success criteria
- Dependencies
- Milestones (alpha, beta, launch)

### STEP 6: TIMELINE_PROMPT
Execution Timeline
- Week-by-week plan (12 weeks)
- Specific tasks per week
- Task ownership (roles)
- Critical path
- Assumptions

---

## Input Template (For Best Results)

When asked for startup idea, structure it like this:

```
PROBLEM:
[Describe the pain point that customers have]

SOLUTION:
[How does your product solve this problem?]

TARGET USERS:
[Who exactly are the customers? Job titles, company size, use cases]

DIFFERENTIATION:
[Why is this better than existing solutions?]

BUSINESS MODEL:
[How do you make money? Pricing strategy?]

CONSTRAINTS:
[Budget, timeline, team size assumptions]
```

**Example:**
```
PROBLEM:
Engineers spend 2-3 hours weekly on code review bottlenecks, delaying deployments

SOLUTION:
AI-powered code review assistant that checks for security, performance, style issues
automatically before human review. Integrates with GitHub/GitLab.

TARGET USERS:
Engineering teams at startups/scale-ups (10-50 engineers) using Python, Go, Java

DIFFERENTIATION:
Pre-trained on security patterns, fixes 60% of issues automatically without
human review. Fastest feedback loop (30 seconds vs 2 hours).

BUSINESS MODEL:
SaaS subscription: $99/month for up to 10 developers

CONSTRAINTS:
$50K budget, 2 engineers + 1 founder, 10-week runway
```

---

## Output Levels

### Level 1: Quick Read (5 minutes)
- Focus on "Feasibility Verdict" (YES/NO)
- Check "Time to MVP" and "Budget"
- Review "Top 3 Risks"

### Level 2: Decision Making (15 minutes)
- Read all of Step 1 (Feasibility)
- Read all of Step 2 (Market)
- Review Step 3 key risks
- Check MVP features and timeline

### Level 3: Execution Planning (30 minutes)
- Study entire 6-step report thoroughly
- Deep dive into MVP roadmap (Step 5)
- Understand week-by-week timeline (Step 6)
- Identify your critical path

### Level 4: Deep Dive (60+ minutes)
- Read entire report with notes
- Cross-reference risks with timeline
- Validate assumptions with research
- Create implementation plan

---

## Common Scenarios

### Scenario 1: Deciding Between 3 Ideas
```bash
# Analyze each idea separately
python main.py
# [Run 3 times with different ideas]

# Compare them
from utils import compare_ideas
report1 = load_analysis_report("analysis_001.json")
report2 = load_analysis_report("analysis_002.json")
compare_ideas(report1, report2)
```

### Scenario 2: Getting Investor Feedback
```bash
# Run analysis
python main.py

# Use output for:
- Market size (Step 2)
- Feasibility (Step 1) 
- Risk mitigation (Step 3)
- MVP roadmap (Step 5)
- 12-week execution plan (Step 6)
```

### Scenario 3: Refining an Idea
```bash
# First analysis
python main.py

# Review feedback from Step 4 (Idea Improvement)
# Revise based on:
- What features to remove
- Core hypothesis clarity
- MVP feature set

# Run analysis again with refined idea
python main.py
```

### Scenario 4: Pre-Seed Fundraising
```bash
# Run analysis with:
- Team background (in constraints)
- Current progress (if any)
- Funding goal and use

# Use output for pitch deck:
- Market opportunity (Step 2)
- Differentiation (Step 2)
- Product roadmap (Step 5)
- Timeline (Step 6)
```

---

## Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| API key error | Create .env with GROQ_API_KEY=your_key |
| API request failed | Check internet, wait 60 seconds, retry |
| Timeout/slow response | Normal: 30-60 seconds. Check connection. |
| Vague output | Provide more detail in your idea description |
| Want different format | Edit prompts/prompts.py, modify output format |
| Want different model | Edit config.py, change MODEL_NAME |
| Want to analyze batch | Use example_usage.py or modify main.py |

---

## Model Options (Groq)

```python
# Option 1: Fastest (Good for iterations)
MODEL_NAME = "llama-3.1-8b-instant"

# Option 2: Best balance (RECOMMENDED)
MODEL_NAME = "llama-3.1-70b-versatile"

# Option 3: Highest quality (Slower)
MODEL_NAME = "llama-3.1-405b-reasoning"
```

Edit `config.py` to change model.

---

## Key Metrics by Industry

Use when providing your idea context:

### SaaS
- Monthly Recurring Revenue (MRR)
- Customer Acquisition Cost (CAC)
- Lifetime Value (LTV)
- Churn rate
- Contract value (ACV)

### Marketplace
- Network effects strategy
- Liquidity (supply vs demand balance)
- Take rate (commission)
- GMV (Gross Merchandise Value)

### B2B
- Sales cycle length
- Enterprise requirements
- Pilot program feasibility
- Contract complexity

### B2C
- User acquisition cost (CAC)
- Daily/Monthly Active Users (DAU/MAU)
- Retention rate
- Viral coefficient

### Mobile App
- App store approval timeline
- User retention metrics
- Download targets
- Monetization model

### Deep Tech
- R&D timeline
- Patent strategy
- Talent requirements
- Time to first revenue

---

## Next Steps Checklist

After analysis, do this:

- [ ] **Understand** - Read all 6 steps, take notes
- [ ] **Validate** - Talk to 10 target users about the problem
- [ ] **Refine** - Adjust idea based on feedback
- [ ] **Plan** - Create detailed task breakdown from timeline
- [ ] **Build** - Start Phase 1 of MVP roadmap
- [ ] **Measure** - Track metrics mentioned in success criteria
- [ ] **Iterate** - Share MVP with users, gather feedback
- [ ] **Scale** - Move to Phase 2 when Phase 1 complete

---

## File Organization Tips

### Save Analysis by Date
```bash
mkdir analyses_2026
mv analysis_*.json analyses_2026/
```

### Organize by Industry
```bash
mkdir saas marketplace hardtech
# Save relevant analyses in each folder
```

### Version Control
```bash
git init
git add .
git commit -m "Initial startup validator agent"
```

---

## Configuration Quick Reference

**config.py:**
- GROQ_API_KEY: Your API key (from .env)
- MODEL_NAME: Which Groq model to use

**prompts/prompts.py:**
- IDEA_ANALYSIS_PROMPT: Feasibility evaluation
- MARKET_ANALYSIS_PROMPT: Market opportunity
- RISK_ANALYSIS_PROMPT: Risk assessment
- FEATURE_PROMPT: MVP features
- MVP_PROMPT: Roadmap
- TIMELINE_PROMPT: Execution plan

**.env:**
- GROQ_API_KEY=gsk_your_key_here

---

## API Usage Tips

### Free Tier
- Usually free credits included
- Check groq.com for current limits

### Cost Optimization
- Use 8b model for early iterations (faster, cheaper)
- Use 70b for final analysis (better quality)
- No per-API-call cost (per minute based)

### Rate Limiting
- API may limit requests
- If hit limit: wait 60 seconds before retry
- Sequential execution prevents issues

---

## Common Mistakes to Avoid

❌ **Too vague:** "A productivity app"
✅ **Specific:** "Calendar app that uses AI to auto-schedule meetings by analyzing attendee preferences and locations"

❌ **Too long:** 10 paragraphs of details
✅ **Concise:** 3-4 structured paragraphs with key info

❌ **No constraints:** Asking for perfect conditions
✅ **Realistic:** "2 engineers, $50K budget, 3-month runway"

❌ **No context:** "What about this?"
✅ **Complete:** Problem, solution, users, differentiation, constraints

---

## Useful Links

- Groq Console: https://console.groq.com
- Groq API Docs: https://console.groq.com/docs
- GitHub: https://github.com/groq/groq-python
- HackerNews: Great for validation ideas

---

**Remember:** This agent is your thinking partner, not your decision-maker. Always validate with real users and data.
