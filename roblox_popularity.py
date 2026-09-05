import os
import requests

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

url = "https://games.roblox.com/v1/games/list"

params = {
    "sortToken": "",
    "gameSetTargetId": 1,
    "maxRows": 10
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

games = data.get("games", [])

if not games:
    requests.post(WEBHOOK, json={
        "content": "⚠️ I couldn't retrieve Roblox trending games right now."
    })
    raise SystemExit

message = "🔥 **Roblox Trending Games**\n\n"

for i, game in enumerate(games[:10], 1):
    name = game.get("name", "Unknown Game")
    players = game.get("playing", 0)
    message += f"**{i}. {name}** — 👥 {players:,} players\n"

requests.post(WEBHOOK, json={
    "content": message
})
