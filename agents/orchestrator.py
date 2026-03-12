from channels.youtube.upload import upload

def run(task):
    if task == "youtube_upload":
        return upload(
            video_path="video.mp4",
            title="Test Upload",
            description="Uploaded via orchestrator",
            tags=["automation", "test"],
            privacy="private"
        )

    print(f"Unknown task: {task}")
