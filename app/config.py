import os
from pathlib import Path


secret_path = os.getenv("SECRET_PATH")

if not secret_path:
    raise RuntimeError("SECRET_PATH environment variable is not set")

api_key = Path(secret_path).read_text().strip()
