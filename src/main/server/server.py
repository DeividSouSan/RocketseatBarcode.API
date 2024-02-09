from flask import Flask
from src.main.routes.tag_routes import tags_routes_bp

app = Flask(__name__)

# Assim você importa as rotas que estão associadas a essa bluepring
app.register_blueprint(tags_routes_bp)
