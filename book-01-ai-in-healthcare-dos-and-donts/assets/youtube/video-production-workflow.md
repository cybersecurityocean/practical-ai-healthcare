# YouTube Video Production Workflow (Open-Source, Free)

> **Channel:** Practical AI Healthcare
> **Format:** Talking-head podcast (your face + your cloned voice)
> **Tools:** 100% open-source from GitHub, zero cost

---

## The Pipeline (per video)

```
Script → Voice Clone → Talking Head Video → Background/Overlay → Edit → Upload
```

**Step 1:** Write script (Google Docs / Markdown)
**Step 2:** Clone your voice (Voicebox — local, free)
**Step 3:** Generate talking-head video (SoulX-FlashHead on Colab — free GPU)
**Step 4:** Add podcast background + mic overlay (Canva free / OBS)
**Step 5:** Edit final video (CapCut free / DaVinci Resolve free)
**Step 6:** Upload to YouTube with thumbnail (Canva free)

---

## Tool 1: Voice Cloning — Voicebox

**What:** Clone your voice from a 10-second audio sample. Generate speech from any script.
**Why:** No paid API needed. Runs locally on your Windows machine.
**GitHub:** https://github.com/jamiepine/voicebox
**Stars:** 50,000+ | **License:** MIT

### Setup (Windows)
1. Download MSI installer from https://voicebox.sh/download/windows
2. Install and launch
3. Go to **Voices** → **Add Voice** → record 10-30 seconds of yourself speaking naturally
4. Voicebox auto-clones your voice

### Generate Audio per Video
1. Open Voicebox → **Generate** tab
2. Paste your script
3. Select your cloned voice
4. Click Generate → export as `.wav` or `.mp3`

### Tips for Best Voice Clone Quality
- Record in a quiet room (no fan/AC noise)
- Speak naturally, at your normal pace
- Include varied intonation (questions, emphasis, pauses)
- 15-30 seconds of reference audio is ideal
- Re-record reference if output sounds robotic

---

## Tool 2: Talking Head Video — SoulX-FlashHead (Google Colab)

**What:** Takes your photo + audio → generates a talking-head video with lip sync.
**Why:** Runs on free Colab GPU (T4). 1.3B parameter model — lightest option.
**GitHub:** https://github.com/Soul-AILab/SoulX-FlashHead
**Stars:** 993 | **License:** Apache 2.0
**HuggingFace Demo:** https://huggingface.co/spaces/Soul-AILab/SoulX-FlashHead

### Option A: HuggingFace Demo (Easiest — No Setup)
1. Go to https://huggingface.co/spaces/Soul-AILab/SoulX-FlashHead
2. Upload your **photo** (clear, front-facing, good lighting)
3. Upload your **audio** (from Voicebox)
4. Click Generate → download video
5. **Limitation:** may have queue wait times

### Option B: Google Colab (Faster — More Control)
1. Open Colab → new notebook
2. Clone the repo:
```python
!git clone https://github.com/Soul-AILab/SoulX-FlashHead.git
%cd SoulX-FlashHead
```
3. Install dependencies:
```python
!pip install -r requirements.txt
```
4. Download model:
```python
!huggingface-cli download Soul-AILab/SoulX-FlashHead-1_3B --local-dir ./models/SoulX-FlashHead-1_3B
```
5. Run inference:
```python
!python inference.py --image_path /content/your_photo.jpg --audio_path /content/your_audio.wav --output_path /content/output.mp4
```

### Photo Requirements for Best Results
- Front-facing, looking at camera
- Neutral or slight smile expression
- Good lighting (no harsh shadows)
- Plain or clean background (will be replaced)
- Resolution: at least 512×512
- No sunglasses, no hands covering face

---

## Tool 3: Podcast Set Background

**What:** Add a podcast studio background behind your talking head.
**Why:** Makes it look professional — mic, laptop, studio lighting.

### Option A: Canva (Free — Recommended)
1. Open Canva → create YouTube thumbnail size (1920×1080)
2. Search "podcast studio" in Elements → pick a background
3. Download as PNG
4. Use as the **first frame** for SoulX-FlashHead (it uses this as the reference image)

### Option B: Real Background
- Sit in front of a clean wall with a bookshelf or plants
- Add a visible USB mic on desk
- This becomes your reference image — no compositing needed

### Option C: OBS Virtual Background
- Use OBS Studio (free) to composite your talking head over a podcast background
- Record the generated video playing in a window → capture with OBS

---

## Tool 4: Video Editing

### CapCut (Free — Recommended for Beginners)
- Download: https://www.capcut.com
- Import your talking-head video
- Add: intro/outro, text overlays, subscribe button, end screen
- Export as 1080p MP4

### DaVinci Resolve (Free — Professional)
- Download: https://www.blackmagicdesign.com/products/davinciresolve
- Full NLE editor, color grading, audio mixing
- Steeper learning curve but industry-standard

---

## Tool 5: Thumbnail Design (Canva Free)

1. Canva → YouTube Thumbnail template (1280×720)
2. Elements: bold text + your face photo + book cover
3. Style: navy/teal palette (matching book brand)
4. Example text: "15 AI Mistakes Hospitals Make"
5. Download as PNG

---

## Video Format Template

```
0:00 - Hook (5-10 sec) — you talking, direct to camera
0:10 - Intro — channel name + topic
0:30 - Body — main content (chapters, numbered points)
4:00 - Summary — key takeaways
4:30 - CTA — "Get the free guide" + link
4:45 - Outro — subscribe + next video
```

---

## First Video: Step-by-Step

### Script
See YouTube Channel Kit → Video Script #1: "AI in Healthcare: 15 Do's & Don'ts"

### Production Steps
1. **Record voice** in Voicebox using your cloned voice
   - Paste the script → generate → download `.wav`
2. **Prepare photo**
   - Take a clean front-facing photo (phone camera is fine)
   - Or use Canva to create a podcast-set composite
3. **Generate video** on Colab or HuggingFace
   - Upload photo + audio → generate → download `.mp4`
4. **Edit** in CapCut
   - Trim, add intro/outro, add text overlays, add subscribe button
5. **Create thumbnail** in Canva
6. **Upload** to YouTube
   - Title, description, tags from the channel kit
   - Pin the Gumroad link as first comment

---

## Future Server Rental (When Ready)

When you're ready to produce 2+ videos/week, rent a GPU server:

| Provider | GPU | VRAM | Cost/month | Best For |
|---|---|---|---|---|
| RunPod | RTX 4090 | 24GB | ~$0.40/hr | SoulX-FlashHead real-time |
| Vast.ai | RTX 3090 | 24GB | ~$0.20/hr | Budget option |
| Lambda | A10G | 24GB | ~$0.60/hr | Reliability |
| Google Colab Pro | T4/A100 | 15-40GB | $10/mo | Upgrade from free tier |

**When to upgrade:** After you've validated the pipeline with free Colab and are ready to scale.

---

## Quick Reference — All Tools

| Tool | Purpose | GitHub | Cost |
|---|---|---|---|
| **Voicebox** | Voice cloning + TTS | jamiepine/voicebox | Free (MIT) |
| **SoulX-FlashHead** | Talking head video | Soul-AILab/SoulX-FlashHead | Free (Apache 2.0) |
| **Canva** | Thumbnails + backgrounds | canva.com | Free tier |
| **CapCut** | Video editing | capcut.com | Free |
| **OBS Studio** | Screen/window capture | obsproject.com | Free (MIT) |
| **DaVinci Resolve** | Pro video editing | blackmagicdesign.com | Free |
