from agent.idea_analyzer import analyze_idea
from agent.market_analyzer import analyze_market
from agent.risk_analyzer import analyze_risk
from agent.feature_generator import generate_features
from agent.mvp_planner import plan_mvp
from agent.timeline_planner import generate_timeline
import sys

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*80}")
    print(f"  {title}")
    print(f"{'='*80}\n")

def print_subsection(title):
    """Print a formatted subsection header"""
    print(f"\n--- {title} ---\n")

def run_agent():
    """Main agent execution loop"""
    print("\n" + "="*80)
    print("  AUTONOMOUS STARTUP VALIDATOR AGENT")
    print("="*80)
    print("\nProvide your startup idea and I will analyze it comprehensively across:")
    print("  1. Feasibility Analysis")
    print("  2. Market Analysis")
    print("  3. Risk Identification")
    print("  4. Idea Improvement & MVP Design")
    print("  5. MVP Roadmap (Phases)")
    print("  6. Execution Timeline (12 weeks)")
    print("\n" + "-"*80 + "\n")
    
    idea = input("📝 Enter your startup idea (be detailed): ").strip()
    
    if not idea:
        print("❌ No idea provided. Exiting.")
        sys.exit(1)
    
    print("\n" + "="*80)
    print("  ANALYZING YOUR STARTUP IDEA...")
    print("="*80)
    print(f"\nIdea: {idea}\n")
    print("Running autonomous analysis across all 6 dimensions...")
    print("(This may take 30-60 seconds)\n")
    
    # STEP 1: FEASIBILITY ANALYSIS
    print_section("STEP 1: FEASIBILITY ANALYSIS")
    try:
        feasibility = analyze_idea(idea)
        print(feasibility)
    except Exception as e:
        print(f"❌ Error in feasibility analysis: {e}")
        return
    
    # STEP 2: MARKET ANALYSIS
    print_section("STEP 2: MARKET ANALYSIS")
    try:
        market = analyze_market(idea)
        print(market)
    except Exception as e:
        print(f"❌ Error in market analysis: {e}")
        return
    
    # STEP 3: RISK IDENTIFICATION
    print_section("STEP 3: RISK IDENTIFICATION")
    try:
        risks = analyze_risk(idea)
        print(risks)
    except Exception as e:
        print(f"❌ Error in risk analysis: {e}")
        return
    
    # STEP 4: IDEA IMPROVEMENT & MVP FEATURES
    print_section("STEP 4: IDEA IMPROVEMENT & MVP FEATURE DEFINITION")
    try:
        features = generate_features(idea)
        print(features)
    except Exception as e:
        print(f"❌ Error in feature generation: {e}")
        return
    
    # STEP 5: MVP PLANNING
    print_section("STEP 5: MVP ROADMAP (PHASED DEVELOPMENT)")
    try:
        mvp = plan_mvp(idea)
        print(mvp)
    except Exception as e:
        print(f"❌ Error in MVP planning: {e}")
        return
    
    # STEP 6: EXECUTION TIMELINE
    print_section("STEP 6: EXECUTION TIMELINE (12 WEEKS)")
    try:
        timeline = generate_timeline(idea)
        print(timeline)
    except Exception as e:
        print(f"❌ Error in timeline generation: {e}")
        return
    
    # COMPLETION
    print_section("ANALYSIS COMPLETE")
    print("✅ Full 6-step autonomous analysis complete.")
    print("\nNext steps:")
    print("  1. Review all recommendations carefully")
    print("  2. Validate market assumptions with real users")
    print("  3. Assemble your core team")
    print("  4. Begin Phase 1 of MVP development")
    print("  5. Measure and iterate based on user feedback")
    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    run_agent()
