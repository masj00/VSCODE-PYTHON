import os
from dotenv import load_dotenv
import requests

# indlæs .env filen
load_dotenv()

# hent API_KEY fra .env
api_key = os.getenv("API_KEY")

# brug API-nøglen
url = "https://api.eksempel.dk/data"
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(url, headers=headers)
print(response.status_code, response.json())

#python -m pip install requests installer den til pc
#