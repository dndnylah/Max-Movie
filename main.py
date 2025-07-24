import requests
import random

# Step 1: Fetch top anime list
response = requests.get('http://127.0.0.1:5000/api/movies')

if response.status_code == 200:
    data = response.json()
    
    if data:
        # Step 2: Pick a random anime
        random_pick = random.choice(data)
        
        # Step 3: Print details
        print("🎬 Title:", random_pick['title'])
        print("📍 Platform:", random_pick['platform'])
        print("📊 Status:", random_pick['status'])
    else:
        print("No anime found in the top list.")
else:
    print(f"Request failed with status code {response.status_code}")
