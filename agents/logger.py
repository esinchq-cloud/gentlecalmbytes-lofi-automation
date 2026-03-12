import json
from datetime import datetime

def log_post(platform, result):
    entry = {
        "platform": platform,
        "result": result,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("post_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
