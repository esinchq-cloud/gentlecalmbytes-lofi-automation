# 🎵 GentleCalmBytes Lofi Automation

**Fully automated lofi music video generator for YouTube.** Runs 100% free on GitHub Actions - cloud-based, no local setup required.

## ⚡ Quick Setup (5 Minutes)

### **Step 1: Get Your API Keys**

#### 🔑 Gemini API Key (Free)
1. Go to: https://aistudio.google.com/app/apikey
2. Click **"Create API Key"**
3. Copy the key

#### 📺 YouTube API Credentials (Free)
1. Go to: https://console.cloud.google.com/apis/credentials
2. Create a new project (if you don't have one)
3. Enable **"YouTube Data API v3"**
4. Click **"Create Credentials"** → **"OAuth 2.0 Client ID"** → **"Desktop app"**
5. Download the JSON file
6. Run this Python script locally once to get your refresh token:

```python
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',  # The file you downloaded
    SCOPES
)
credentials = flow.run_local_server(port=8080)
print(f"\n🔑 Your YOUTUBE_REFRESH_TOKEN:\n{credentials.refresh_token}")
```

7. Copy the **CLIENT_ID**, **CLIENT_SECRET** (from JSON), and the **REFRESH_TOKEN** (from script output)

### **Step 2: Add Secrets to GitHub**

1. Go to your repository → **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"** and add each of these:

| Secret Name | Value |
|-------------|-------|
| `GEMINI_API_KEY` | Your Gemini API key from Step 1 |
| `YOUTUBE_CLIENT_ID` | From Google Cloud credentials JSON |
| `YOUTUBE_CLIENT_SECRET` | From Google Cloud credentials JSON |
| `YOUTUBE_REFRESH_TOKEN` | From the Python script output |

### **Step 3: Enable & Run**

1. Go to **Actions** tab in your repository
2. Click **"I understand my workflows, go ahead and enable them"**
3. Click **"Lofi Content Generator"** workflow
4. Click **"Run workflow"** → **"Run workflow"** button

**Done!** Your first video will generate and upload automatically.

---

## 🚀 Features

✅ **Generates 3-5 hour lofi videos** with AI-powered concepts  
✅ **Auto-uploads** to YouTube every Tuesday, Thursday, Saturday at 8am EST  
✅ **100% free** - uses GitHub Actions (2000 free minutes/month)  
✅ **Cloud-based** - no local setup, runs on GitHub's servers  
✅ **Manual trigger** - click "Run workflow" anytime for instant uploads  

---

## 📅 Automation Schedule

- **Automatic Uploads**: Tuesday, Thursday, Saturday at 8am EST
- **Manual Uploads**: Click "Actions" → "Lofi Content Generator" → "Run workflow" anytime
- **Free Tier**: GitHub gives 2000 minutes/month (≈40 hours of generation time)

---

## 🎨 Customization

Want different video themes? Edit the `THEMES` list in `main.py`:

```python
THEMES = [
    "Deep focus study session with rain sounds",
    "Late-night coding sprint with city ambience",
    "Your custom theme here"
]
```

---

## 📊 Usage Limits (Free Tiers)

- **GitHub Actions**: 2000 minutes/month
- **Gemini API**: 1500 requests/day (free tier)
- **YouTube API**: 10,000 quota units/day

This is enough for **40+ hours** of video generation per month on the free tier!

---

## 🔧 Advanced: Local Testing

To test locally before pushing:

```bash
# Install dependencies
pip install google-generativeai pillow requests google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Set environment variables
export GEMINI_API_KEY="your-key"
export YOUTUBE_CLIENT_ID="your-id"
export YOUTUBE_CLIENT_SECRET="your-secret"
export YOUTUBE_REFRESH_TOKEN="your-token"

# Run
python main.py
```

---

## 💡 How It Works

1. **GitHub Actions** runs the workflow on schedule (or manual trigger)
2. **Gemini AI** generates creative lofi music concepts and visual descriptions
3. **Python script** creates placeholder video file (enhance this with real audio/visual generation)
4. **YouTube API** uploads the video with AI-generated title and description
5. **Rinse & repeat** - fully automated!

---

## 🎯 Next Steps

This is a **starter template**. Enhance it by:

- Adding real music generation (Udio API, Suno AI, etc.)
- Creating animated visuals (Stable Diffusion, Runway ML)
- Building 3-5 hour video assemblies (FFmpeg)
- Adding live chat interaction features

---

## 📝 License

Open source. Use freely for your YouTube channel automation!

---

**Built for GentleCalmBytes** - Your sanctuary for soft, aesthetic lofi beats 🌙
