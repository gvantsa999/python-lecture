def main():
    spacecraft = {
        "name": "james webb space telescope",
    }
    
    # დაემატა მრგვალი ფრჩხილები update-სთვის
    spacecraft.update({
        "distance": 0.01,
        "orbit": "sun"
    })
    
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
========== REPORT ==========

Name: {spacecraft.get("name", "unknown").title()}
Distance: {spacecraft.get("distance", "unknown")} AU
Orbit: {spacecraft.get("orbit", "unknown")}

============================
"""

main()