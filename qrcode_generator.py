import requests
import json
import os
from tkinter import Tk, filedialog

class QRCodeGenerate:
    def __init__(self):
        self.url = "https://api.qrserver.com/v1/create-qr-code/"

    def func(self):
        os.system("cls" if os.name == "nt" else "clear")
        text = input("Enter text or link you want to create QR code for: ")
        params = {
            "data": text,
            "size": "300x300"
        }

        try:
            response = requests.get(self.url, params=params)
            if response.status_code != 200:
                print(f"API request failed. Status code: {response.status_code}")
                print(f"Response body: {response.text}")
                return

            with open("QR.png", "wb") as f:
                f.write(response.content)

            print("QR code saved as QR.png")
            os.system("QR.png" if os.name == "nt" else "xdg-open QR.png")

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
