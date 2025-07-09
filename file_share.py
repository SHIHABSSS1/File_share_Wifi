import os
import zipfile
from flask import Flask, request, send_from_directory, render_template_string, redirect, send_file
from werkzeug.utils import secure_filename
from io import BytesIO
from urllib.parse import unquote, quote

app = Flask(__name__)
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Jinja2 filter for URL encoding
def url_encode(s):
    return quote(s)

app.jinja_env.filters['url_encode'] = url_encode

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WiFi File Share</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container py-5">
        <h1 class="mb-4 text-center">📤 Upload Your Files</h1>

        <form method="POST" enctype="multipart/form-data" class="mb-5">
            <div class="input-group">
                <input type="file" name="files" class="form-control" multiple required>
                <button type="submit" class="btn btn-primary">Upload</button>
            </div>
        </form>

        <h2 class="mb-3">📁 Uploaded Files</h2>

        <form method="POST" action="/download-zip">
            <ul class="list-group mb-3">
                {% for file in files %}
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div class="d-flex align-items-center gap-2">
                        <input type="checkbox" name="selected_files" value="{{ file }}"> 
                        <a href="/uploads/{{ file|url_encode }}" target="_blank">{{ file }}</a>
                    </div>
                    <div>
                        <a href="/uploads/{{ file|url_encode }}" class="btn btn-sm btn-outline-primary" download="{{ file }}">Download</a>
                    </div>
                </li>
                {% endfor %}
            </ul>
            <div class="d-flex gap-2">
                <button type="submit" class="btn btn-success">⬇ Download Selected as ZIP</button>
                <a href="/download-all-zip" class="btn btn-outline-primary">📦 Download All Files</a>
            </div>
        </form>
    </div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_files = request.files.getlist("files")
        for file in uploaded_files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_DIR, filename))
        return redirect("/")
    
    files = os.listdir(UPLOAD_DIR)
    return render_template_string(HTML_TEMPLATE, files=files)

@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    filename = unquote(filename)
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)

@app.route("/download-zip", methods=["POST"])
def download_zip():
    selected_files = request.form.getlist("selected_files")
    if not selected_files:
        return "No files selected.", 400

    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for filename in selected_files:
            file_path = os.path.join(UPLOAD_DIR, filename)
            if os.path.exists(file_path):
                zf.write(file_path, arcname=filename)

    memory_file.seek(0)
    return send_file(memory_file, download_name="selected_files.zip", as_attachment=True)

@app.route("/download-all-zip")
def download_all_zip():
    files = os.listdir(UPLOAD_DIR)
    if not files:
        return "No files available.", 400

    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for filename in files:
            file_path = os.path.join(UPLOAD_DIR, filename)
            if os.path.isfile(file_path):
                zf.write(file_path, arcname=filename)

    memory_file.seek(0)
    return send_file(memory_file, download_name="all_files.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
