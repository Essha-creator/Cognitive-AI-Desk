import requests
import json
import os

class Aicheck:
    def __init__(self):
        self.url = "https://ai-content-identifier2.p.rapidapi.com/text"
        self.headers = {
            "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
	        "x-rapidapi-host": "ai-content-identifier2.p.rapidapi.com",
	        "Content-Type": "application/json"
        }

    def func(self):
        os.system("cls" if os.name == "nt" else "clear")
        text = input("Enter the text : ")

        payload = {
            "text": text,
            "threshold": 10
        }

        try:
            response = requests.post(self.url, headers=self.headers, json=payload)

            if response.status_code != 200:
                print(f"API request failed. Status code: {response.status_code}")
                print("Response:", response.text)
                return

            data = response.json()

            percentage = data['data']['percentage']
            total_words = data['data']['stats']['totalWords']
            ai_words = data['data']['stats']['aiWords']
            human_words = data['data']['stats']['humanWords']

            print("\n AI Detection Results:")
            print(f"AI Percentage : {percentage}%")
            print(f"Total Words   : {total_words}")
            print(f"AI Words      : {ai_words}")
            print(f"Human Words   : {human_words}")

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)




