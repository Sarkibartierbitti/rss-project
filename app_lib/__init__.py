from flask import Flask, request, render_template, url_for
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables
# Create the Flask application instance
app = Flask(__name__)


app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")  # Get from .env

# Import routes after creating the app to avoid circular imports
from app_lib import routes
