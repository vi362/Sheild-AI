from flask import Flask
from src.routes.main import main_bp
from src.routes.proxy import proxy_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(proxy_bp)

if __name__ == '__main__':
    app.run(debug=True)
