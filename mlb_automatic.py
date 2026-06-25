import json
import requests
from datetime import datetime

def get_mlb_games():
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"https://api.mlb.com/schedule?sportId=1&date={today}"
    
    try:
        r = requests.get(url, timeout=15)
        data = r.json()
        
        games = []
        for date in data.get("dates", []):
            for game in date.get("games", []):
                home_team = game["teams"]["home"]["team"]
                away_team = game["teams"]["away"]["team"]
                
                game_time = game["gameDate"][11:16]  # HH:MM
                
                games.append({
                    "league": "MLB",
                    "time": game_time,
                    "home": home_team["name"],
                    "away": away_team["name"],
                    "homeLogo": f"https://a.espncdn.com/i/teamlogos/mlb/500/{home_team['abbreviation'].lower()}.png",
                    "awayLogo": f"https://a.espncdn.com/i/teamlogos/mlb/500/{away_team['abbreviation'].lower()}.png",
                    "link": f"https://sportsrdlive.blogspot.com/2026/06/{len(games)+1}er-juego-del-dia.html"
                })
        return games
    except:
        return []

# ================== GENERAR JSON ==================
def main():
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    mlb_games = get_mlb_games()
    
    full_data = {
        today_str: mlb_games
        # Aquí puedes agregar manualmente FIFA si quieres
    }
    
    with open('matches.json', 'w', encoding='utf-8') as f:
        json.dump(full_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ matches.json actualizado con {len(mlb_games)} partidos MLB ({today_str})")

if __name__ == "__main__":
    main()
