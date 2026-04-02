import requests
import datetime

def get_pistons_scores():
    # URL for NBA scoreboard JSON data
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for HTTP errors
        data = response.json()
        
        pistons_found = False
        print(f"Pistons Scores for {datetime.date.today()}:")
        print("-" * 40)
        
        # Iterate through events (games)
        for event in data['events']:
            # Check if Pistons are playing
            if "Pistons" in event['shortName']:
                pistons_found = True
                
                # Get competition details
                comp = event['competitions'][0]
                date = comp['date']
                status = comp['status']['type']['description']
                
                # Team details
                home_team = comp['competitors'][0]['team']['displayName']
                home_score = comp['competitors'][0]['score']
                away_team = comp['competitors'][1]['team']['displayName']
                away_score = comp['competitors'][1]['score']
                
                print(f"Status: {status}")
                print(f"{away_team} {away_score} @ {home_team} {home_score}")
                print("-" * 40)
                
        if not pistons_found:
            print("No Pistons games found for today.")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_pistons_scores()

