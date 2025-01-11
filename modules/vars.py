import os

API_ID    = os.environ.get("API_ID", "20868701")
API_HASH  = os.environ.get("API_HASH", "9bf50346c886503948931272bbdab967")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
