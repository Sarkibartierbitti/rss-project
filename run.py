from app_lib import app  # Import the app instance from the package
import os
import secrets
from pathlib import Path
from dotenv import load_dotenv
from typing import *

# 1. Define the path to the .env file (in the script's directory)
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"


if not ENV_FILE.exists():
    secret_key = secrets.token_urlsafe(32)
    with open(ENV_FILE, "w") as f:
        f.write(f"SECRET_KEY={secret_key}\n")
    print("Generated new .env file with SECRET_KEY")


# 3. Load existing .env (whether just created or pre-existing)
load_dotenv(ENV_FILE)

# 4. Retrieve the secret key
SECRET_KEY = os.getenv("SECRET_KEY")

# 5. Verify the key exists (safety check)
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY not found in .env")


if __name__ == "__main__":
    app.run(debug=True) 
