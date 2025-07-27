# Background Music Extractor

This repository contains a simple web application that extracts background music from an uploaded song.
It uses `pydub` to approximate vocal removal by subtracting stereo channels.

## Requirements
- Python 3.12+
 - `flask`
 - `pydub`

- `ffmpeg` in your PATH for audio conversion

Install dependencies:
```bash
pip install flask pydub

```

## Running the app
```bash
python server.py
```
Then open `http://localhost:5000` in your browser and upload a song. The app
will return a `background.wav` file containing the approximated instrumental.
Uploads are sent to `/api/process` both locally and on Vercel.

## Deploying to Vercel
Vercel will automatically detect the Python function in `api/process.py`. The
static `index.html` at the repository root loads the app and sends requests to
`/api/process`, which is handled by that serverless function.

1. Install the Vercel CLI and run `vercel` to deploy.
2. Ensure `ffmpeg` is available in your deployment environment (Vercel build
   step) for audio conversion.

