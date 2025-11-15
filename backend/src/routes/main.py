from flask import Blueprint, render_template
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path to frontend templates
frontend_templates = os.path.join(project_root, "frontend", "templates")

# Register blueprint with correct path
main_bp = Blueprint(
    "main",
    __name__,
    template_folder=frontend_templates
)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/home")
def home():
    return render_template("home.html")
