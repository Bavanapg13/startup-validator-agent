# Autonomous Startup Validator Agent

An AI-powered autonomous agent that evaluates, analyzes, and plans startup ideas using a structured 6-step methodology.

## Overview

This agent behaves like an **experienced startup co-founder and investor combined**. It analyzes startup ideas across six critical dimensions and provides actionable, realistic recommendations for execution.

## Features

### 6-Step Autonomous Analysis

1. **Feasibility Analysis** – Evaluates technical complexity, timeline, cost, team requirements, and dependencies
2. **Market Analysis** – Identifies target users, market size, demand, competition, and differentiation
3. **Risk Identification** – Analyzes technical, market, execution, financial, and regulatory risks
4. **Idea Improvement** – Refines scope, removes non-essential features, strengthens value proposition
5. **MVP Planning** – Creates phased roadmap (typically 3-4 phases of 2-4 weeks each)
6. **Execution Timeline** – Generates detailed week-by-week plan for 12 weeks

## Setup

### Prerequisites
- Python 3.8+
- Groq API key
- `pip install -r requirements.txt`

### Installation

1. Clone or navigate to the project folder
2. Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

3. Install dependencies:
```bash
pip install groq python-dotenv
```

### Configuration

Edit `config.py` if needed:
```python
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # From .env file
MODEL_NAME = "llama-3.1-8b-instant"  # Groq model (or any other available model)
```

## Usage

Run the agent:
```bash
python main.py
```

You'll be prompted to enter your startup idea. Provide as much detail as possible:

**Example Input:**
```
A mobile app that uses AI to analyze photos of food and provides personalized 
nutrition recommendations based on your health goals and dietary restrictions. 
It integrates with wearables to track calories burned and provides meal planning.
```

The agent will then run through all 6 analysis steps and generate a comprehensive report.

## Output Structure

The agent outputs a structured analysis report with:

- **Technical Complexity:** Low/Medium/High rating with explanation
- **Timeline Estimate:** Weeks to MVP
- **Budget Estimate:** Rough cost breakdown
- **Team Requirements:** Roles and headcount
- **Market Size & Demand:** TAM and urgency signals
- **Competition:** Direct competitors and differentiation
- **Risks:** Categorized by type with mitigation strategies
- **MVP Features:** 3-5 essential features only
- **Phased Roadmap:** Development phases with milestones
- **Week-by-Week Timeline:** 12-week execution plan

## How It Works

### Agent Architecture

```
main.py (Entry point)
  ├── idea_analyzer.py (Step 1: Feasibility)
  ├── market_analyzer.py (Step 2: Market)
  ├── risk_analyzer.py (Step 3: Risks)
  ├── feature_generator.py (Step 4: MVP Features)
  ├── mvp_planner.py (Step 5: MVP Roadmap)
  └── timeline_planner.py (Step 6: Timeline)
  
prompts/ (Detailed system prompts for each analysis step)
config.py (Configuration & API credentials)
```

### Execution Flow

1. **User Input** → Startup idea description
2. **Feasibility Analysis** → Can it be built?
3. **Market Analysis** → Is there demand?
4. **Risk Analysis** → What could go wrong?
5. **Feature Definition** → What's the MVP?
6. **MVP Planning** → How to build it?
7. **Timeline** → When to build what?
8. **Output** → Comprehensive report with actionable recommendations

## Agent Behavior

The agent is designed to:

- ✅ Make **autonomous, reasoned decisions** without asking unnecessary questions
- ✅ Reason **step-by-step** using startup frameworks and best practices
- ✅ Provide **clear, structured, and concise** output
- ✅ Focus on **realistic, early-stage constraints** (limited budget, small teams)
- ✅ Avoid **vague advice** – every recommendation is specific and actionable
- ✅ Think like a **co-founder and investor** combined

The agent is **NOT** a chatbot. It's goal-driven, autonomous, and designed to help startup teams execute.

## Prompts Reference

All analysis prompts are in `prompts/prompts.py`. Each prompt includes:

- **System instruction** (role and context)
- **Detailed evaluation criteria**
- **Output format specification**
- **Key dimensions to analyze**

### Prompt Examples

**IDEA_ANALYSIS_PROMPT:** Evaluates feasibility with technical complexity, timeline, budget, and team requirements.

**MARKET_ANALYSIS_PROMPT:** Identifies target users, market size, demand signals, competition, and differentiation.

**RISK_ANALYSIS_PROMPT:** Analyzes technical, market, execution, financial, and regulatory risks with mitigation strategies.

**FEATURE_PROMPT:** Suggests improvements, removes non-essential scope, and defines MVP features.

**MVP_PROMPT:** Creates phased roadmap with milestones and success criteria.

**TIMELINE_PROMPT:** Week-by-week execution plan with task ownership.

## Example Analysis

### Input:
```
A SaaS platform that automates customer support using AI, 
integrating with help desk tools like Zendesk and Intercom.
```

### Output Includes:
```
STEP 1: FEASIBILITY ANALYSIS
- Technical Complexity: High (requires API integrations, NLP, training)
- Estimated Time to MVP: 8-10 weeks
- Budget Estimate: $20,000-$40,000 (servers, tools, initial hiring)
- Team Size: 2 engineers, 1 founder, 0.5 designer part-time
- Critical Dependencies: Zendesk/Intercom API access, LLM API (OpenAI/Groq)
- Feasibility Verdict: YES - technically feasible with experienced team

STEP 2: MARKET ANALYSIS
- Target Users: Support teams at SMBs (20-500 employees)
- Market Size: $5B+ (customer support software market growing 15%/year)
- Demand Signal: 60% of support teams report overwhelm, need automation
- Top 3 Competitors: [Details on how you differentiate]
- Unique Value Proposition: Pre-trained on support patterns, 80%+ first-response resolution

STEP 3: RISK IDENTIFICATION
[Detailed risks with severity, impact, and mitigation]

STEP 4: IDEA IMPROVEMENT & MVP FEATURES
[What to remove, core hypothesis, 5 MVP features]

STEP 5: MVP ROADMAP
[4 phases with deliverables and success criteria]

STEP 6: EXECUTION TIMELINE
[Week-by-week breakdown with ownership and milestones]
```

## Customization

### To modify analysis dimensions:
Edit the relevant prompt in `prompts/prompts.py`

### To change the AI model:
Update `MODEL_NAME` in `config.py` (if using Groq, check available models)

### To add new analysis steps:
1. Create a new file in `agent/` folder
2. Add corresponding prompt in `prompts/prompts.py`
3. Import and call in `main.py`

## Requirements

```
groq>=0.4.0
python-dotenv>=1.0.0
```

Install with:
```bash
pip install -r requirements.txt
```

## Troubleshooting

### "GROQ_API_KEY environment variable not set"
- Ensure `.env` file exists in root directory
- Format: `GROQ_API_KEY=sk_your_key_here`
- Reload the terminal after creating `.env`

### API Rate Limiting
- The agent makes 6 sequential API calls (one per analysis step)
- If you hit rate limits, wait 60 seconds before running again

### Timeouts
- Some analyses may take 30-60 seconds depending on API response time
- This is normal; the agent is generating detailed, thoughtful analysis

## Future Enhancements

- [ ] Multi-idea comparison (analyze 2-3 ideas and recommend best)
- [ ] Iterative refinement (ask follow-up questions based on initial analysis)
- [ ] Financial modeling (revenue projections, unit economics)
- [ ] Team recommendations (role requirements, hiring timeline)
- [ ] Funding strategy (what to raise, when, from whom)
- [ ] Competitive benchmarking (detailed competitor analysis)
- [ ] User interview guides (questions to validate assumptions)

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! To improve:

1. Refine prompts for better analysis quality
2. Add new analysis dimensions
3. Improve output formatting
4. Add data storage for analysis history
5. Create comparison reports

## Author

Developed as an autonomous startup validation agent using the Groq API and Claude/LLM-based reasoning.

---

**Remember:** This agent is a tool to accelerate your thinking. Always validate recommendations with real users, real data, and real market feedback.
