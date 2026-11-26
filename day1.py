#Portfolio
projects = [
    {
        "title":   "SMP Performance Coach",
        "problem": "Manually tracking fitness data and writing coaching notes took 30+ minutes per day.",
        "solution":"Automated pipeline that trains a classifier on 28 days of data, predicts daily goal achievement, and generates a coaching message.",
        "tools":   ["Python", "scikit-learn", "pandas", "FastAPI"],
        "result":  "Prediction + coaching in under 2 seconds. Exports weekly JSON report.",
        "github":  "github.com/ronmossmaitha/smp-tracker",
        "type":    "ML + API"
    },
    {
        "title":   "Multi-Endpoint API Dashboard",
        "problem": "Three separate data sources with no unified view. Reporting was manual and inconsistent.",
        "solution":"Dashboard that fetches from three endpoints, processes each independently, and outputs a combined summary with protocol comparison.",
        "tools":   ["Python", "requests", "pandas"],
        "result":  "Single command produces a full multi-source report. Reduced prep time by 90%.",
        "github":  "github.com/ronmossmaitha/api-dashboard",
        "type":    "Data Pipeline"
    },
        {
        "title":    "Legacy Fitness WhatsApp Bot",
        "problem":  "Front desk spent hours answering repetitive WhatsApp inquiries about membership pricing, branch hours, and free trial bookings.",
        "solution": "Automated webhook server that handles incoming WhatsApp messages via Infobip API and routes users through instant self-service menus.",
        "tools":    ["Python", "Flask", "Infobip API", "requests"],
        "result":   "24/7 instant responses across 3 gym branches, eliminating manual FAQ replies and streamlining trial session bookings.",
        "github":   "github.com/ronmossmaitha/legacybot",
        "type":     "Chatbot + API"
    },

    {
        "title":   "Browser-Based AI Coach",
        "problem": "Clients needed a way to get coaching feedback without installing software.",
        "solution":"Client-side JavaScript tool. Prediction engine and coaching generator run entirely in the browser. No server required.",
        "tools":   ["JavaScript", "DOM API", "Fetch API"],
        "result":  "Zero setup for end users. Works on any device with a browser.",
        "github":  "github.com/ronmossmaitha/browser-coach",
        "type":    "Web Tool"
    },
]

SEPARATOR = "=" * 64

print(SEPARATOR)
print("  DEVELOPER PORTFOLIO SUMMARY")
print(SEPARATOR)

for i, p in enumerate(projects, 1):
    print(f"\nProject {i}: {p['title']}  [{p['type']}]")
    print(f"  Problem:  {p['problem']}")
    print(f"  Solution: {p['solution']}")
    print(f"  Tools:    {', '.join(p['tools'])}")
    print(f"  Result:   {p['result']}")
    print(f"  Code:     {p['github']}")

print()
print(SEPARATOR)
print(f"  Total projects: {len(projects)}")
all_tools = set(t for p in projects for t in p["tools"])
print(f"  Tech stack:     {', '.join(sorted(all_tools))}")
print(SEPARATOR)


#Generating Service Offer Text with Python
services = [
    {
        "name":    "Automated Data Reports",
        "client":  "small business owners who export data manually",
        "problem": "spending 2-4 hours per week copying data between spreadsheets and writing summaries",
        "outcome": "a Python script that reads their data source and produces a formatted weekly report in under 30 seconds",
        "tools":   "Python, pandas, CSV/Excel/JSON",
        "example": "28-day fitness log analysis with weekly breakdown and protocol comparison"
    },
    {
        "name":    "API Integration Scripts",
        "client":  "operations teams using two or more disconnected tools",
        "problem": "manually copying data between platforms with no automation between them",
        "outcome": "a Python script that pulls from one API and pushes to another automatically on a schedule",
        "tools":   "Python, requests, FastAPI, JSON",
        "example": "Multi-endpoint dashboard pulling from three simulated SMP data sources"
    },
    {
        "name":    "AI Writing Automation",
        "client":  "business owners who write the same types of responses repeatedly",
        "problem": "spending hours writing first drafts of emails, summaries, or customer responses",
        "outcome": "a Python tool that generates structured drafts using the OpenAI API in the required voice and format",
        "tools":   "Python, OpenAI API, python-dotenv",
        "example": "SMP coaching message generator that mirrors the Chat API response structure"
    },
]

for i, s in enumerate(services, 1):
    print(f"SERVICE {i}: {s['name'].upper()}")
    print()
    print(f"  Who I help:    {s['client']}")
    print(f"  Their problem: {s['problem']}")
    print(f"  What I deliver:{s['outcome']}")
    print(f"  Tools used:    {s['tools']}")
    print(f"  Proof of work: {s['example']}")
    print()

    # Generate a one-line pitch
    pitch = (f"I help {s['client']} by building {s['outcome'].split('a ')[1] if 'a ' in s['outcome'] else s['outcome']}.")
    print(f"  One-line pitch: \"{pitch}\"")
    print("-" * 60)


#Project Rate Calculator
def calculate_project_rate(
    hours_estimated,
    hourly_target,       # what you want to earn per hour
    complexity_factor,   # 1.0 = standard, 1.3 = complex, 1.5 = very complex
    revision_buffer=0.2, # 20% buffer for revisions
    market_floor=150,    # minimum charge for any project
):
    """Calculate a project price from time estimate and target rate."""
    base_cost  = hours_estimated * hourly_target
    with_complexity = base_cost * complexity_factor
    with_buffer     = with_complexity * (1 + revision_buffer)
    final_price = max(with_buffer, market_floor)

    return {
        "hours_estimated":  hours_estimated,
        "hourly_target":    hourly_target,
        "base_cost":        round(base_cost),
        "with_complexity":  round(with_complexity),
        "with_buffer":      round(with_buffer),
        "quote_price":      round(final_price / 50) * 50,  # round to nearest $50
    }

# Define the projects to quote
projects = [
    {
        "name":               "Automated weekly CSV report",
        "hours_estimated":    8,
        "hourly_target":      35,
        "complexity_factor":  1.0,
    },
    {
        "name":               "FastAPI + Supabase integration",
        "hours_estimated":    20,
        "hourly_target":      40,
        "complexity_factor":  1.3,
    },
    {
        "name":               "Full SMP tracker tool with dashboard",
        "hours_estimated":    50,
        "hourly_target":      45,
        "complexity_factor":  1.5,
    },
]

SEPARATOR = "=" * 58
print(SEPARATOR)
print("  PROJECT QUOTE CALCULATOR")
print(SEPARATOR)

for p in projects:
    result = calculate_project_rate(
        hours_estimated   = p["hours_estimated"],
        hourly_target     = p["hourly_target"],
        complexity_factor = p["complexity_factor"],
    )
    print(f"\nProject: {p['name']}")
    print(f"  Hours estimated: {result['hours_estimated']}h")
    print(f"  Base cost:       ${result['base_cost']:,}  ({result['hours_estimated']}h x ${result['hourly_target']}/h)")
    print(f"  With complexity: ${result['with_complexity']:,}  (x{p['complexity_factor']} factor)")
    print(f"  With 20% buffer: ${result['with_buffer']:,}")
    print(f"  Quote price:     ${result['quote_price']:,}  (rounded to nearest $50)")

print()
print(SEPARATOR)
