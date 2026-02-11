import os
import json
import time
import requests
from datetime import datetime
import google.generativeai as genai
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# Configure Gemini
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Video themes for lofi content
THEMES = [
    "Deep focus study session with rain sounds",
    "Late-night coding sprint with city ambience",
    "Peaceful morning reading with birds chirping",
    "Relaxation after work with sunset vibes",
    "Background ambience for creative work"
]

def generate_music_concept():
    theme = THEMES[datetime.now().day % len(THEMES)]
    prompt = f"Create a detailed lofi hip hop music description for: {theme}. Include: tempo, instruments, mood, and 3-hour progression structure."
    response = model.generate_content(prompt)
    return response.text

def generate_visual_concept():
    prompt = "Describe a calming lofi visual scene with: animated cozy environment (study room, cafe, or nature), subtle movements (rain, snow, leaves), warm color palette, perfect for 3-5 hour loop"
    response = model.generate_content(prompt)
    return response.text

def create_placeholder_video():
    with open('output.mp4', 'w') as f:
        f.write("Placeholder for generated video")
    return 'output.mp4'

def upload_to_youtube(video_path, title, description):
    credentials = Credentials(
        token=None,
        refresh_token=os.environ['YOUTUBE_REFRESH_TOKEN'],
        token_uri='https://oauth2.googleapis.com/token',
        client_id=os.environ['YOUTUBE_CLIENT_ID'],
        client_secret=os.environ['YOUTUBE_CLIENT_SECRET']
    )
    
    youtube = build('youtube', 'v3', credentials=credentials)
    
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['lofi', 'study', 'relax', 'chill beats', 'focus music'],
            'categoryId': '10'
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False
        }
    }
    
    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
    request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
    response = request.execute()
    return f"https://youtube.com/watch?v={response['id']}"

if __name__ == "__main__":
    print("🎵 Generating lofi content...")
    music_concept = generate_music_concept()
    visual_concept = generate_visual_concept()
    print(f"Music: {music_concept[:100]}...")
    print(f"Visual: {visual_concept[:100]}...")
    video_file = create_placeholder_video()
    title = f"Lofi Hip Hop - {THEMES[datetime.now().day % len(THEMES)]} [3 Hours]"
    description = f"🎵 {title}\n\n{music_concept}\n\nPerfect for:\n✨ Deep focus study sessions (3-8 hours)\n✨ Remote work & coding sprints\n✨ Reading, writing & journaling\n✨ Late-night relaxation & sleep\n\n{visual_concept}\n\n🔔 Subscribe to GentleCalmBytes for daily lofi uploads!\n📅 New streams: Tuesday, Thursday, Saturday at 8am EST\n🌙 24/7 live stream coming soon\n\nAll music is original. All visuals are crafted for calm.\n\n#lofi #studymusic #chillbeats #focusmusic"
    video_url = upload_to_youtube(video_file, title, description)
    print(f"✅ Uploaded: {video_url}")
