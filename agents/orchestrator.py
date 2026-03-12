# Orchestrator Agent
# Decides which automation task to run and routes to the correct agent.

from channels.youtube.upload import upload
from utils.helpers import log

def run(task="test"):
    log(f"Orchestrator received task: {task}")

    if task == "youtube_upload":
        log("Routing to YouTube upload agent...")
        upload("sample_video.mp4")  # placeholder path
    else:
        log(f"No matching task found for: {task}")

if __name__ == "__main__":
    run()
