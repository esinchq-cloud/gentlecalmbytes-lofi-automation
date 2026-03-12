from orchestrator import dispatch
from agent.selector import choose_platforms
from agent.formatter import format_for_platform
from agent.logger import log_post
from agent.optimizer import optimize_strategy

def autopilot(content):
    # Step 1: optimizer decides best platforms
    platforms = optimize_strategy(content)

    results = []

    for platform in platforms:
        formatted = format_for_platform(platform, content)
        result = dispatch(platform, formatted["action"], **formatted["payload"])
        log_post(platform, result)
        results.append(result)

    return results
