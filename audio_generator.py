import requests
import json
import os
from tkinter import Tk, filedialog



class AudioGenerate:
    def __init__(self):
        self.url = "https://text-to-speach-english.p.rapidapi.com/makevoice"
        self.headers = {
            "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
            "x-rapidapi-host": "text-to-speach-english.p.rapidapi.com",
            "Content-Type": "application/json"
        }
        
    def func(self):
        os.system("cls" if os.name == "nt" else "clear")
        text = input("Write text to convert to AI voice: ")
        Params = {"text": text}
        payload = {
	"key1": "value",
	"key2": "value"
}
        try:
            response = requests.post(self.url,json=payload, headers=self.headers, params=Params)
            if response.status_code != 200:
                print(f"API request failed. Status code: {response.status_code}")
                return

            with open("audio.mp3", "wb") as f:
                f.write(response.content)

            print("Audio saved as audio.mp3")
            os.system("audio.mp3" if os.name == "nt" else "xdg-open audio.mp3")

        except Exception as e:
            print("Error:", e)


