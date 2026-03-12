import json
from agent.selector import choose_platforms

def analyze_performance():
    earnings = {}
    try:
        with open("post_log.json", "r") as f:
            for line in f:
                entry = json.loads(line)
                platform = entry["platform"]
                earnings[platform] = earnings.get(platform, 0) + 1
    except FileNotFoundError:
        return {}

    return earnings

def optimize_strategy(content):
    performance = analyze_performance()

    # If no data yet, fallback to selector
    if not performance:
        return choose_platforms(content)

    # Sort platforms by performance
    sorted_platforms = sorted(performance.items(), key=lambda x: x[1], reverse=True)

    # Pick top 3 earning platforms
    top_platforms = [p[0] for p in sorted_platforms[:3]]

    return top_platforms
