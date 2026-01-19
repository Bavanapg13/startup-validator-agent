"""
Example usage of the Startup Validator Agent

This script demonstrates how to use the agent with different startup ideas.
Run: python example_usage.py
"""

from agent.idea_analyzer import analyze_idea
from agent.market_analyzer import analyze_market
from agent.risk_analyzer import analyze_risk
from agent.feature_generator import generate_features
from agent.mvp_planner import plan_mvp
from agent.timeline_planner import generate_timeline

# Example startup ideas to analyze
EXAMPLE_IDEAS = [
    """
    A mobile-first SaaS platform that uses AI to automate repetitive customer support 
    tasks. It integrates with popular help desk tools like Zendesk and Intercom, learns 
    from support patterns, and responds to common questions automatically, escalating 
    complex issues to humans. Targets small to mid-size e-commerce and SaaS companies 
    (100-500 employees) currently spending $5K-50K/month on support.
    """,
    
    """
    A B2B marketplace connecting freelance engineers with companies needing short-term 
    technical talent. Unlike Toptal/Upwork, it focuses exclusively on backend engineers 
    and DevOps specialists, with 1-3 month projects. Built-in code review, automated 
    vetting, and escrow payment system.
    """,
    
    """
    An iOS app for fitness enthusiasts that gamifies workout consistency. Users form 
    squads, compete in monthly challenges, earn points for workouts, and unlock rewards 
    (discounts at gyms, sports brands). Integrates with Apple Health and popular fitness 
    apps (Strava, MyFitnessPal).
    """,
]

def run_example_analysis(idea, example_num=1):
    """Run a complete analysis for a given idea"""
    
    print(f"\n{'='*80}")
    print(f"  EXAMPLE {example_num}: STARTUP IDEA ANALYSIS")
    print(f"{'='*80}")
    print(f"\nIdea: {idea.strip()}\n")
    print("Running autonomous 6-step analysis...\n")
    
    analyses = {
        "feasibility": analyze_idea(idea),
        "market": analyze_market(idea),
        "risks": analyze_risk(idea),
        "features": generate_features(idea),
        "mvp": plan_mvp(idea),
        "timeline": generate_timeline(idea),
    }
    
    # Print Feasibility
    print(f"\n{'─'*80}")
    print("STEP 1: FEASIBILITY ANALYSIS")
    print(f"{'─'*80}")
    print(analyses["feasibility"])
    
    # Print Market
    print(f"\n{'─'*80}")
    print("STEP 2: MARKET ANALYSIS")
    print(f"{'─'*80}")
    print(analyses["market"])
    
    # Print Risks
    print(f"\n{'─'*80}")
    print("STEP 3: RISK IDENTIFICATION")
    print(f"{'─'*80}")
    print(analyses["risks"])
    
    # Print Features
    print(f"\n{'─'*80}")
    print("STEP 4: IDEA IMPROVEMENT & MVP FEATURES")
    print(f"{'─'*80}")
    print(analyses["features"])
    
    # Print MVP Roadmap
    print(f"\n{'─'*80}")
    print("STEP 5: MVP ROADMAP")
    print(f"{'─'*80}")
    print(analyses["mvp"])
    
    # Print Timeline
    print(f"\n{'─'*80}")
    print("STEP 6: EXECUTION TIMELINE")
    print(f"{'─'*80}")
    print(analyses["timeline"])
    
    return analyses

if __name__ == "__main__":
    print("\n" + "="*80)
    print("  STARTUP VALIDATOR AGENT - EXAMPLE ANALYSIS")
    print("="*80)
    print(f"\nThis script demonstrates the agent with {len(EXAMPLE_IDEAS)} example ideas.\n")
    
    # Ask which example to run
    print("Available examples:")
    for i, idea in enumerate(EXAMPLE_IDEAS, 1):
        preview = idea.strip()[:80] + "..."
        print(f"  {i}. {preview}")
    
    choice = input("\nEnter example number (1, 2, 3, or 'all'): ").strip()
    
    if choice.lower() == 'all':
        for i, idea in enumerate(EXAMPLE_IDEAS, 1):
            run_example_analysis(idea, i)
    elif choice in ['1', '2', '3']:
        idx = int(choice) - 1
        run_example_analysis(EXAMPLE_IDEAS[idx], int(choice))
    else:
        print("Invalid choice. Please run the script again.")
