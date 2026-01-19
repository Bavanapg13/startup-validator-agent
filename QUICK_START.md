# Quick Start Guide

Get the Autonomous Startup Validator Agent running in 5 minutes.

## Step 1: Get Groq API Key (2 minutes)

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up (free) if you don't have an account
3. Create an API key
4. Copy the key (format: `gsk_...`)

## Step 2: Setup Environment (2 minutes)

1. In the project root folder, create a `.env` file:

```
GROQ_API_KEY=gsk_your_actual_key_here
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

(Or manually: `pip install groq python-dotenv`)

## Step 3: Run the Agent (1 minute)

```bash
python main.py
```

You'll see:
```
================================================================================
  AUTONOMOUS STARTUP VALIDATOR AGENT
================================================================================

Provide your startup idea and I will analyze it comprehensively across:
  1. Feasibility Analysis
  2. Market Analysis
  3. Risk Identification
  4. Idea Improvement & MVP Design
  5. MVP Roadmap (Phases)
  6. Execution Timeline (12 weeks)

📝 Enter your startup idea (be detailed): 
```

## Step 4: Provide Your Startup Idea

Example input:
```
A mobile app that connects local farmers directly to restaurants, 
eliminating middlemen. Real-time inventory, quality photos, 
pricing negotiations, logistics coordination. Targets small restaurants 
in tier-2 cities looking for fresh ingredients at lower costs.
```

Press Enter and wait 30-60 seconds for analysis.

## What You'll Get

The agent will output a comprehensive report with:

✅ **Feasibility Analysis**
- Can it be built? Timeline? Budget? Team size?

✅ **Market Analysis**  
- Who are the users? How big is the market? Who competes?

✅ **Risk Analysis**
- What could go wrong? How to mitigate?

✅ **MVP Feature Design**
- What should you actually build first?

✅ **Phased Roadmap**
- Break development into 3-4 achievable phases

✅ **12-Week Timeline**
- Week-by-week execution plan with task ownership

## Tips for Best Results

### 1. Be Detailed with Your Idea
❌ Bad: "A productivity app"
✅ Good: "A project management tool specifically for remote design teams that integrates with Figma and Slack, auto-syncing design changes to task statuses"

### 2. Include Context
✅ Mention your target user
✅ Explain the problem being solved
✅ Describe your differentiation
✅ Note any constraints (budget, team, timeline)

### 3. Example Template

```
Problem: [What's the pain point?]
Solution: [How does your product solve it?]
Target Users: [Who are they?]
Differentiation: [Why is this better than existing solutions?]
Constraints: [Budget limits, team size, timeline]
```

## File Structure

```
startup-validator-agent/
├── main.py                 # Main agent entry point (RUN THIS)
├── config.py              # API configuration
├── requirements.txt       # Python dependencies
├── .env                   # Your API key (CREATE THIS)
├── .env.example           # Template for .env
├── README.md              # Full documentation
├── QUICK_START.md         # This file
├── ADVANCED_CONFIG.md     # Advanced customization
├── utils.py               # Utility functions
├── example_usage.py       # Example analyses
│
├── agent/
│   ├── idea_analyzer.py           # Step 1: Feasibility
│   ├── market_analyzer.py         # Step 2: Market
│   ├── risk_analyzer.py           # Step 3: Risks
│   ├── feature_generator.py       # Step 4: MVP Features
│   ├── mvp_planner.py             # Step 5: Roadmap
│   └── timeline_planner.py        # Step 6: Timeline
│
└── prompts/
    └── prompts.py         # All analysis prompts
```

## Troubleshooting

### Error: "GROQ_API_KEY environment variable not set"

**Solution:**
1. Make sure `.env` file exists in the root directory
2. Check the key format: `GROQ_API_KEY=gsk_...`
3. Restart your terminal
4. Run: `python main.py` again

### Error: "Failed to create a completion"

**Solution:**
- Your API key might be invalid
- Check if you have free credits on Groq console
- Wait 1 minute and try again (rate limiting)

### Timeout or Slow Response

**Solution:**
- The analysis takes 30-60 seconds (normal)
- Check your internet connection
- Groq servers might be busy - try again in a few minutes

### Want Different Output Format?

See `ADVANCED_CONFIG.md` for customization options.

## Try It With Examples

```bash
python example_usage.py
```

This shows 3 pre-built startup ideas with full analysis.

## Next Steps

1. ✅ Run analysis for your idea
2. ✅ Review all 6 steps carefully
3. ✅ Share with your co-founders and get feedback
4. ✅ Validate assumptions with real users
5. ✅ Start building Phase 1 of your MVP

## Need Help?

- **Setup issues:** Check config.py and .env
- **Understanding output:** See README.md
- **Customization:** See ADVANCED_CONFIG.md
- **More examples:** See example_usage.py

## Key Reminders

⚡ This agent is **autonomous** - it makes decisions, not suggestions

💡 This is a **thinking tool** - always validate with real users and data

🚀 Output is **actionable** - you can follow the timeline directly

🎯 Focus on **execution** - the analysis is just the beginning

---

**Ready to analyze? Run:** `python main.py`
