from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload(video_path, title, description, tags=None, privacy="private"):
    # Load OAuth credentials written by GitHub Actions
    creds = Credentials.from_authorized_user_file(
        "client_secret.json",
        ["https://www.googleapis.com/auth/youtube.upload"]
    )

    youtube = build("youtube", "v3", credentials=creds)

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or []
        },
        "status": {
            "privacyStatus": privacy
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = request.execute()
    return response
