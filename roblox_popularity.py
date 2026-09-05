import os
import requests

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

url = "https://games.roblox.com/v1/games"

params = {
    "universeIds": "1818"
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

games = data.get("data", [])

if not games:
    requests.post(WEBHOOK, json={
        "content": "⚠️ Roblox did not return any game data."
    })
    raise SystemExit

game = games[0]

name = game.get("name", "Unknown Game")
players = game.get("playing", 0)

message = (
    "🔥 **Roblox Popularity Test**\n\n"
    f"🎮 **{name}**\n"
    f"👥 Players: **{players:,}**"
)

result = requests.post(WEBHOOK, json={
    "content": message
})

result.raise_for_status()
