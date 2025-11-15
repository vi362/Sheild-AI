import os

# Define project structure
folders = [
    "backend/logs",
    "backend/src/routes",
    "backend/src/models",
    "backend/src/utils",
    "frontend/templates",
    "frontend/static"
]

files = {
    "backend/app.py": "# Main Flask App\n\nfrom src.routes.main import app\n\nif __name__ == '__main__':\n    app.run(debug=True)",
    "backend/requirements.txt": "flask\njoblib\nnumpy\nscipy\nscikit-learn",
    "backend/logs/detections.log": "",

    # Hybrid WAF Modules
    "backend/src/__init__.py": "",
    "backend/src/routes/__init__.py": "",
    "backend/src/routes/main.py": "# Main route handlers\n\nfrom flask import Flask, render_template\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return render_template('index.html')\n\n@app.route('/home')\ndef home():\n    return render_template('home.html')",
    "backend/src/routes/proxy.py": "# Proxy route (To be implemented)\n\nfrom flask import request\n\n# Function to process user request\n# TODO: Add logic later",

    "src/models/__init__.py": "",
    "src/utils/__init__.py": "",
    "src/utils/signature_checker.py": "# Placeholder for signature-based detection",
    "src/utils/preprocessor.py": "# Placeholder for request feature extraction",

    # Templates (Frontend)
    "frontend/templates/index.html": "<html><body><h1>Landing Page</h1><a href='/home'>Check Your Request</a></body></html>",
    "frontend/templates/home.html": "<html><body><h1>Home Page</h1><input type='text' id='requestInput'><button onclick='checkRequest()'>Check Request</button></body></html>",

    # Static Files (JS & CSS)
    "frontend/static/home.js": "function checkRequest() { console.log('Request check triggered'); }"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with initial content
for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Environment setup complete! All files and folders created.")
