"""Telegram Channel API - Python example.

Docs: https://apiserpent.com/telegram-channel-api
Run:  SERPENT_API_KEY=sk_live_... python example.py
"""
import os
import sys

import requests

API_KEY = os.environ.get("SERPENT_API_KEY")
if not API_KEY:
    sys.exit("Set the SERPENT_API_KEY environment variable first.")

params = {"channel": "durov"}

response = requests.get(
    "https://apiserpent.com/api/telegram/channel",
    params=params,
    headers={"X-API-Key": API_KEY},
    timeout=60,
)
response.raise_for_status()
data = response.json()

for item in data.get("posts", []):
    print(" | ".join(str(item.get(k)) for k in ['date', 'views', 'text', 'url']))
