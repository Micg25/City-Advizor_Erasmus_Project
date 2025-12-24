import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get('GEOAPIFY_API_KEY')
print(f"Using API Key: {api_key[:5]}...")

# Test Geoapify Places API for London
url = "https://api.geoapify.com/v2/places"
params = {
    "categories": "tourism",
    "filter": "circle:-0.1278,51.5074,5000", # London
    "limit": 5,
    "apiKey": api_key
}

try:
    response = requests.get(url, params=params)
    print(f"Status: {response.status_code}")
    print(f"URL: {response.url}")
    
    if response.status_code == 200:
        data = response.json()
        features = data.get("features", [])
        print(f"Feature Count: {len(features)}")
        
        for i, f in enumerate(features[:2]):
            props = f.get('properties', {})
            print(f"Item {i+1}: {props.get('name')} - {props.get('formatted')}")
    else:
        print(f"Error Body: {response.text}")
        
except Exception as e:
    print(f"Error: {e}")
