"""
Advanced Configuration Guide for Startup Validator Agent

This file provides detailed configuration options and customization patterns.
"""

# ============================================================================
# 1. MODEL CONFIGURATION
# ============================================================================

# Available Groq Models (as of January 2026):
GROQ_MODELS = {
    "llama-3.1-8b-instant": {
        "speed": "⚡ Very Fast",
        "quality": "Good for analysis",
        "cost": "Low",
        "best_for": "Quick iterations, cost-sensitive"
    },
    "llama-3.1-70b-versatile": {
        "speed": "⚡ Fast", 
        "quality": "Excellent reasoning",
        "cost": "Medium",
        "best_for": "Detailed analysis, best quality"
    },
    "llama-3.1-405b-reasoning": {
        "speed": "⚠️ Slower",
        "quality": "Exceptional analysis",
        "cost": "Higher",
        "best_for": "Complex ideas, detailed breakdown"
    }
}

# Recommendation: Start with llama-3.1-70b-versatile for best balance

# ============================================================================
# 2. PROMPT CUSTOMIZATION PATTERNS
# ============================================================================

# To customize any prompt, modify prompts/prompts.py and:
# - Keep the {idea} placeholder
# - Maintain the structured format
# - Be specific about what outputs you want

CUSTOM_PROMPT_TEMPLATE = """
You are [YOUR ROLE DESCRIPTION].

[CONTEXT AND INSTRUCTION]

When analyzing this startup idea:
1. [Dimension 1]
2. [Dimension 2]
3. [Dimension 3]

Format your response as:
[EXPECTED OUTPUT FORMAT]

Startup Idea:
{idea}
"""

# ============================================================================
# 3. ANALYSIS DEPTH LEVELS
# ============================================================================

DEPTH_LEVELS = {
    "quick": {
        "description": "Quick 5-minute analysis",
        "use_case": "Initial screening",
        "prompt_length": "concise",
        "details": "High-level only"
    },
    "standard": {
        "description": "Full 30-minute analysis (DEFAULT)",
        "use_case": "Primary evaluation",
        "prompt_length": "detailed",
        "details": "Comprehensive across all 6 steps"
    },
    "deep": {
        "description": "Thorough 60+ minute analysis",
        "use_case": "Due diligence before fundraising",
        "prompt_length": "very_detailed",
        "details": "Deep financial modeling, market research, competitive analysis"
    }
}

# To implement: Add depth parameter to prompts

# ============================================================================
# 4. INDUSTRY-SPECIFIC PROMPTS
# ============================================================================

# You can create specialized prompts for different industries
INDUSTRY_TEMPLATES = {
    "saas": "Focus on: Churn, LTV, CAC, monthly recurring revenue (MRR)",
    "marketplace": "Focus on: Network effects, liquidity, supply/demand balance, take rate",
    "mobile_app": "Focus on: App store approval, retention, DAU/MAU, user acquisition",
    "deep_tech": "Focus on: IP/patents, R&D costs, time to revenue, talent requirements",
    "hardware": "Focus on: Manufacturing costs, supply chain, capital intensity, certification",
    "b2b": "Focus on: Sales cycle, enterprise requirements, contract value (ACV)",
    "b2c": "Focus on: Viral loops, content moats, unit economics, unit growth"
}

# ============================================================================
# 5. RISK SCORING SYSTEM (OPTIONAL)
# ============================================================================

# You can implement automatic risk scoring
RISK_SCORES = {
    "feasibility_score": {
        "range": "0-100",
        "high": "70-100 (build this)",
        "medium": "40-70 (assess carefully)",
        "low": "0-40 (reconsider or pivot)"
    },
    "market_score": {
        "range": "0-100",
        "high": "70-100 (strong TAM)",
        "medium": "40-70 (niche market)",
        "low": "0-40 (small addressable market)"
    },
    "risk_score": {
        "range": "0-100 (higher = more risk)",
        "low": "0-30 (low risk profile)",
        "medium": "31-70 (manageable risks)",
        "high": "71-100 (high risk, high reward)"
    }
}

# ============================================================================
# 6. MULTI-IDEA COMPARISON WEIGHTS
# ============================================================================

# If comparing multiple ideas, use these weights
COMPARISON_WEIGHTS = {
    "feasibility": 0.25,      # Can we actually build this?
    "market_size": 0.30,      # Is the market big enough?
    "competition": 0.15,      # How crowded is the space?
    "risk_profile": 0.20,     # How risky is this?
    "founder_fit": 0.10       # Do we have the right background?
}

# Scoring formula: Sum(score * weight) for each dimension

# ============================================================================
# 7. TIMELINE ACCELERATION FACTORS
# ============================================================================

# Modify MVP timeline based on team composition
TIMELINE_FACTORS = {
    "founding_team_has_domain_expertise": 0.7,    # Reduce timeline by 30%
    "have_existing_codebase": 0.8,                # Reduce timeline by 20%
    "first_time_founders": 1.3,                   # Increase timeline by 30%
    "have_designer": 1.0,                         # No change
    "bootstrapped_budget": 1.2,                   # Increase timeline by 20%
    "have_seed_funding": 1.0,                     # No change
}

# ============================================================================
# 8. BATCH ANALYSIS CONFIG (FOR FUTURE ENHANCEMENT)
# ============================================================================

# To analyze multiple ideas in batch:
BATCH_CONFIG = {
    "max_ideas": 5,
    "parallel_processing": False,      # Set True for concurrent API calls
    "save_results": True,
    "output_format": "json",           # or "csv", "markdown"
    "comparison_report": True
}

# ============================================================================
# 9. ADVANCED PROMPTING TECHNIQUES
# ============================================================================

# Few-shot learning example (to improve prompt quality):
EXAMPLE_ANALYSIS = """
EXAMPLE:
Idea: "An AI tool that converts Figma designs to React code"

FEASIBILITY: High
- Technical: Medium (design parsing + code generation)
- Time: 10 weeks for MVP
- Budget: $30K
- Team: 2 engineers, 1 founder

MARKET: Medium-sized niche
- Target: Frontend developers/design teams
- TAM: ~$500M (design tools market segment)
- Differentiation: Accuracy > competitors, Figma-native

RISKS: [Technical: API changes, Legal: IP/licensing, Market: Free alternatives]

MVP: Core features only (parse Figma, generate React components, review interface)
"""

# You can add examples to prompts for better outputs

# ============================================================================
# 10. EXECUTION ROADMAP TEMPLATES
# ============================================================================

# Template for how to structure MVP phases
MVP_PHASE_TEMPLATE = {
    "phase_1_foundation": {
        "duration": "2-3 weeks",
        "focus": "Prototype + core infrastructure",
        "tasks": ["Setup dev environment", "Build core logic", "API integrations"],
        "deliverable": "Working prototype",
        "success_metric": "Prototype works without errors"
    },
    "phase_2_development": {
        "duration": "2-3 weeks", 
        "focus": "Build MVP features",
        "tasks": ["Implement features", "UI/UX", "Testing"],
        "deliverable": "Feature-complete beta",
        "success_metric": "All MVP features working"
    },
    "phase_3_launch": {
        "duration": "1-2 weeks",
        "focus": "Launch readiness",
        "tasks": ["Polish", "Documentation", "User testing"],
        "deliverable": "Production-ready MVP",
        "success_metric": "First 20 users sign up"
    }
}

# ============================================================================
# 11. INTEGRATION OPTIONS (FOR FUTURE ENHANCEMENT)
# ============================================================================

# Potential integrations to add:
FUTURE_INTEGRATIONS = {
    "stripe_api": "For revenue projections and pricing analysis",
    "openai_embeddings": "For competitive analysis similarity scoring",
    "database": "To store and compare analyses over time",
    "slack": "To send analysis reports to Slack",
    "google_sheets": "To export timelines for project management",
    "pitch_deck_generator": "To automatically create investor pitch decks"
}

# ============================================================================
# 12. ANALYSIS QUALITY CHECKLIST
# ============================================================================

# Use this to validate analysis completeness
QUALITY_CHECKLIST = {
    "feasibility": [
        "✓ Technical complexity assessed",
        "✓ Timeline estimated in weeks",
        "✓ Budget with specific breakdown",
        "✓ Team composition defined",
        "✓ Clear YES/NO verdict with reasoning"
    ],
    "market": [
        "✓ Target user persona described",
        "✓ Market size (TAM) estimated",
        "✓ Demand signals explained",
        "✓ 2-3 competitors listed with comparison",
        "✓ Clear differentiation stated"
    ],
    "risks": [
        "✓ 3+ technical risks identified",
        "✓ 3+ market risks identified",
        "✓ 2+ execution risks identified",
        "✓ Each risk has severity and mitigation",
        "✓ No vague or generic risks"
    ],
    "features": [
        "✓ Features removed explained",
        "✓ Core hypothesis stated clearly",
        "✓ 3-5 MVP features (not more)",
        "✓ Each feature has 'why essential' reasoning",
        "✓ Out-of-scope list defined"
    ],
    "mvp": [
        "✓ 3-4 phases defined",
        "✓ Each phase has 2-4 week duration",
        "✓ Clear deliverables per phase",
        "✓ Success criteria defined",
        "✓ Dependencies between phases noted"
    ],
    "timeline": [
        "✓ Week-by-week breakdown for 12 weeks",
        "✓ Specific tasks per week (not vague)",
        "✓ Owner assigned to each task",
        "✓ Key milestones marked",
        "✓ Critical path identified"
    ]
}

# ============================================================================
# IMPLEMENTATION GUIDE
# ============================================================================

"""
To use these configurations:

1. CHANGE MODEL:
   Edit config.py: MODEL_NAME = "llama-3.1-70b-versatile"

2. CUSTOMIZE PROMPTS:
   Edit prompts/prompts.py, add your industry context

3. ADD RISK SCORING:
   Create a new file: agent/risk_scorer.py
   Implement scoring logic based on RISK_SCORES

4. ENABLE BATCH ANALYSIS:
   Create agent/batch_analyzer.py
   Process multiple ideas sequentially or in parallel

5. ADD DATABASE:
   Install SQLAlchemy or MongoDB
   Store analyses for historical comparison

6. CREATE INTEGRATIONS:
   Add Slack, Google Sheets connectors
   Export reports to team tools
"""

print(__doc__)
