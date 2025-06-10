import requests
import ujson   # acts like json module
import os
import base64
import tkinter as tk
from tkinter import filedialog


class BackgroundRemove:
    def __init__(self):
        self.api2_url = "https://background-removal4.p.rapidapi.com/v1/results"
        self.api2_headers = {
            "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
            "x-rapidapi-host": "background-removal4.p.rapidapi.com",
        }

    def choose_file(self):
        root = tk.Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)

        file_path = filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")]
        )

        root.destroy()

        if not file_path:
            print("No file selected.")
            return None 

        print(f"[INFO] Selected file: {file_path}")
        return file_path 
    def use_api2(self, file_path):
        try:
            with open(file_path, 'rb') as image_file:
                image_data = image_file.read()

            boundary = "----011000010111000001101001"
            filename = os.path.basename(file_path)

            payload = (
                f"--{boundary}\r\n"
                f"Content-Disposition: form-data; name=\"image\"; filename=\"{filename}\"\r\n"
                f"Content-Type: image/jpeg\r\n\r\n"
            ).encode('utf-8') + image_data + f"\r\n--{boundary}--\r\n".encode('utf-8')

            headers = self.api2_headers.copy()
            headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"

            response = requests.post(self.api2_url, headers=headers, data=payload)

            if response.status_code != 200:
                print(f"API 2 Error: {response.status_code} - {response.text}")
                return

            # data = response.json()
            # import ujson

            data = ujson.loads(response.text)

            base64_img = data['results'][0]['entities'][0]['image']

            with open("output_api2.png", "wb") as f:
                f.write(base64.b64decode(base64_img))

            print(" Background removed and saved as output_api2.png")
            os.system("output_api2.png" if os.name == "nt" else "xdg-open output_api2.png")

        except Exception as e:
            print("API 2 Error:", e)

    def func(self):
        file_path = self.choose_file()
        if file_path:
            print("\nUsing Background Removal API (base64 in JSON)...")
            self.use_api2(file_path)


