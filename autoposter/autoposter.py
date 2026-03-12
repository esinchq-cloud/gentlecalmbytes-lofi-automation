import os
import importlib
from orchestrator import dispatch

def get_available_platforms():
    platforms = []
    channels_path = "channels"

    for item in os.listdir(channels_path):
        full_path = os.path.join(channels_path, item)
        if os.path.isdir(full_path):
            platforms.append(item)

    return platforms

def autopost(content):
    platforms = get_available_platforms()
    results = []

    for platform in platforms:
        try:
            # Try to load the platform's post module
            module = importlib.import_module(f"channels.{platform}.post")

            # Standard payload for all platforms
            formatted = {
                "action": "post",
                "payload": {"text": content}
            }

            # Send to orchestrator
            result = dispatch(platform, formatted["action"], **formatted["payload"])

            results.append({
                "platform": platform,
                "status": "success",
                "result": result
            })

        except ModuleNotFoundError:
            # Platform has no post.py file
            results.append({
                "platform": platform,
                "status": "no_post_function"
            })

        except Exception as e:
            # Any other error
            results.append({
                "platform": platform,
                "status": "error",
                "error": str(e)
            })

    return results
