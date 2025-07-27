# Background Music Extractor

This repository contains a simple Flask web application that extracts background music from a song. It uses `pydub` to perform a basic vocal removal by subtracting stereo channels.

## Requirements
- Python 3.12+
- `flask`, `pydub`, `librosa`, `soundfile`
- `ffmpeg` in your PATH for audio conversion

Install dependencies:
```bash
pip install flask pydub librosa soundfile
```

## Running the app
```bash
python server.py
```
Then open `http://localhost:5000` in your browser and upload a song. The app will return a `background.wav` file containing the approximated instrumental.
