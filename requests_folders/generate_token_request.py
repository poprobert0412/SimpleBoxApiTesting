import random
import requests

def generate_token():
    num = random.randint(1, 99999999999999)
    data = {
        "clientName": "Random Name",
        "clientEmail": f"random_email{num}@yahoo.com"
    }
    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=data)
    return response.json()["accessToken"]
