import requests
import base64
import os
import tkinter as tk
from tkinter import filedialog

class ColorizeImage:
    def __init__(self):
        self.url = "https://image-colorize.p.rapidapi.com/image/effects/colourize"
        self.headers = {
            "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
            "x-rapidapi-host": "image-colorize.p.rapidapi.com"
        }

    def choose_file(self):
        root = tk.Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)

        file_path = filedialog.askopenfilename(
            title="Select a Black & White Image File",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")]
        )

        root.destroy()

        if not file_path:
            print("No file selected.")
            return None

        print(f"[INFO] Selected file: {file_path}")
        return file_path

    def func(self):
        os.system("cls" if os.name == "nt" else "clear")

        image_path = self.choose_file()
        if not image_path:
            return

        if not os.path.isfile(image_path):
            print("File does not exist at the given path.")
            return

        with open(image_path, "rb") as image_file:
            files = {"image": image_file}
            response = requests.post(self.url, headers=self.headers, files=files)

        if response.status_code != 200:
            print(f"API request failed. Status code: {response.status_code}")
            print("Response:", response.text)
            return

        try:
            result = response.json()
            base64_image = result["image"]
            image_data = base64.b64decode(base64_image)

            output_file = "clroutput.png"
            with open(output_file, "wb") as f:
                f.write(image_data)

            print(f"Colorized image saved as {output_file}")

          
            try:
                if os.name == "nt":
                    os.startfile(output_file)
                elif os.uname().sysname == "Darwin":
                    os.system(f"open {output_file}")
                else:
                    os.system(f"xdg-open {output_file}")
            except Exception as e:
                print("Could not open image automatically:", e)

        except Exception as e:
            print("Failed to parse response or decode image:", e)
            print("Raw response:", response.text)
