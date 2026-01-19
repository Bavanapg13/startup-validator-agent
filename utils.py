"""
Utility functions for the Startup Validator Agent
Includes: report saving, analysis comparison, JSON export
"""

import json
from datetime import datetime
import os

def save_analysis_report(idea, analysis_results):
    """
    Save analysis results to a JSON file with timestamp
    
    Args:
        idea (str): The startup idea description
        analysis_results (dict): Dictionary containing all analysis steps
    
    Returns:
        str: Path to saved file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"analysis_{timestamp}.json"
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "idea": idea,
        "analysis": analysis_results
    }
    
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✅ Analysis saved to: {filename}")
    return filename

def load_analysis_report(filename):
    """Load a previously saved analysis report"""
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return None
    
    with open(filename, 'r') as f:
        return json.load(f)

def compare_ideas(idea1_report, idea2_report):
    """
    Compare two startup analysis reports side-by-side
    
    Args:
        idea1_report (dict): First analysis report
        idea2_report (dict): Second analysis report
    
    Returns:
        dict: Comparison metrics
    """
    comparison = {
        "idea_1": idea1_report.get("idea"),
        "idea_2": idea2_report.get("idea"),
        "comparison": {}
    }
    
    print("\n" + "="*80)
    print("  STARTUP IDEAS COMPARISON")
    print("="*80)
    print(f"\nIDEA 1: {idea1_report.get('idea')}")
    print(f"IDEA 2: {idea2_report.get('idea')}")
    print("\nUse this comparison to identify which idea has better:")
    print("  - Feasibility (technical, timeline, budget)")
    print("  - Market opportunity (size, demand, competition)")
    print("  - Risk profile (technical risks, market risks)")
    print("  - MVP clarity (feature simplicity, execution complexity)")
    
    return comparison

def generate_executive_summary(analysis_results):
    """
    Generate a one-page executive summary from full analysis
    
    Returns:
        str: Formatted summary
    """
    summary = f"""
╔════════════════════════════════════════════════════════════════════════════╗
║                     EXECUTIVE SUMMARY                                      ║
╚════════════════════════════════════════════════════════════════════════════╝

RECOMMENDATION:
[Based on overall feasibility, market opportunity, and risks]

KEY METRICS:
- Feasibility: [✅ High / ⚠️ Medium / ❌ Low]
- Market Opportunity: [✅ Large / ⚠️ Medium / ❌ Small]
- Risk Profile: [✅ Low / ⚠️ Medium / ❌ High]
- Time to MVP: [X weeks]
- Estimated Budget: $[X]
- Team Required: [X people]

TOP 3 STRENGTHS:
1. [Strength]
2. [Strength]
3. [Strength]

TOP 3 RISKS:
1. [Risk with mitigation]
2. [Risk with mitigation]
3. [Risk with mitigation]

NEXT STEPS:
1. Validate [key assumption] with users
2. Build MVP with focus on [core feature]
3. Measure [key metric] to validate market fit

═══════════════════════════════════════════════════════════════════════════════
"""
    return summary

def export_timeline_csv(timeline_data):
    """Export execution timeline to CSV format for project management tools"""
    csv_content = "Week,Phase,Task,Owner,Dependencies,Status\n"
    # Parse timeline_data and format as CSV
    # This is a template - customize based on actual timeline format
    return csv_content

def list_saved_reports():
    """List all saved analysis reports in current directory"""
    reports = [f for f in os.listdir('.') if f.startswith('analysis_') and f.endswith('.json')]
    
    if not reports:
        print("No saved reports found.")
        return []
    
    print("\nSaved Analysis Reports:")
    print("-" * 60)
    for i, report in enumerate(reports, 1):
        print(f"{i}. {report}")
    
    return reports

def archive_old_reports(days=30):
    """
    Archive analysis reports older than specified days
    Creates 'archived/' folder if it doesn't exist
    """
    from pathlib import Path
    import shutil
    
    archive_dir = Path('archived')
    archive_dir.mkdir(exist_ok=True)
    
    now = datetime.now()
    moved_count = 0
    
    for filename in os.listdir('.'):
        if filename.startswith('analysis_') and filename.endswith('.json'):
            filepath = Path(filename)
            file_time = datetime.fromtimestamp(filepath.stat().st_mtime)
            
            if (now - file_time).days > days:
                shutil.move(str(filepath), str(archive_dir / filename))
                moved_count += 1
    
    print(f"✅ Archived {moved_count} reports older than {days} days")

if __name__ == "__main__":
    # Example usage
    print("Startup Validator Agent - Utility Functions")
    print("Import this module to use: save_analysis_report(), load_analysis_report(), etc.")
