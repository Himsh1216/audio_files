import os
import tempfile
from flask import Flask, request, send_file
from background import isolate_background

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    with tempfile.TemporaryDirectory() as tmpdir:
        src_path = os.path.join(tmpdir, 'input')
        dst_path = os.path.join(tmpdir, 'output.wav')
        file.save(src_path)
        isolate_background(src_path, dst_path)
        return send_file(dst_path, as_attachment=True, download_name='background.wav')

def handler(environ, start_response):
    return app(environ, start_response)
