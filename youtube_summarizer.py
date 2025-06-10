import requests
import json
import os
from urllib.parse import urlparse, parse_qs

class Yt_summarizer:
    def __init__(self):
        self.url = "https://youtube-summarizer2.p.rapidapi.com/summarize"
        self.headers = {
            "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
	        "x-rapidapi-host": "youtube-summarizer2.p.rapidapi.com"
        }

    def func(self):
        os.system("cls" if os.name == "nt" else "clear")
        text = input("Enter the Yt url : ")
        video_id = self.extract_video_id(text)
        querystring = {"id":video_id}

        try:
            response = requests.get(self.url, headers=self.headers, params=querystring)

            if response.status_code != 200:
                print(f"API request failed. Status code: {response.status_code}")
                print("Response:", response.text)
                return

            data = response.json()

            summary = data['summary']

            print(f" Summary  : {summary}")

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
    def extract_video_id(self, url):
        parsed = urlparse(url)

        if "youtu.be" in parsed.netloc:
            return parsed.path.strip("/")

        
        if "youtube.com" in parsed.netloc:
            query = parse_qs(parsed.query)
            return query.get("v", [None])[0]

        return None




