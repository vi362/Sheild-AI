import os
from flask import Flask
from src.routes.main import main_bp
from src.routes.proxy import proxy_bp

# backend/app.py directory
backend_dir = os.path.dirname(os.path.abspath(__file__))

# project root = backend/..
project_root = os.path.abspath(os.path.join(backend_dir, ".."))

# frontend folder paths
template_path = os.path.join(project_root, "frontend", "templates")
static_path   = os.path.join(project_root, "frontend", "static")

app = Flask(
    __name__,
    template_folder=template_path,
    static_folder=static_path,
    static_url_path="/static"
)

print(">>> TEMPLATE FOLDER =", template_path)
print(">>> STATIC FOLDER   =", static_path)

# Register routes
app.register_blueprint(main_bp)
app.register_blueprint(proxy_bp)

if __name__ == '__main__':
    app.run(debug=True)
