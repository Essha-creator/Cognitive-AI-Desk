import base64
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import requests
import os
from screeninfo import get_monitors
from tkinter import filedialog
from urllib.parse import urlparse, parse_qs

# === Audio Generator Window === (your original code)
def generate_audio_window():
    win = Toplevel(root)
    win.title("AI Audio Generator")
    win.geometry(f"{screen_width}x{screen_height}")
    win.configure(bg="white")

    bg_img = Image.open("Navy Blue Futuristic Technology Linktree Background (12).png")
    bg_img = bg_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(win, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(win, text="Text to AI Voice", font=("Arial", 28, "bold"),
                  bg="white", fg="#5193B3")
    title.place(relx=0.5, y=80, anchor="center")

    input_label = Label(win, text="Enter your text:", font=("Arial", 20, "bold"),
                        bg="white", fg="black")
    input_label.place(relx=0.5, rely=0.2, anchor="center")

    input_text = Text(win, width=70, height=10, font=("Arial", 14))
    input_text.place(relx=0.5, rely=0.4, anchor="center")

    result_label = Label(win, text="", font=("Arial", 12), bg="white", fg="green")
    result_label.place(relx=0.5, rely=0.65, anchor="center")

    def convert_to_audio():
        text = input_text.get("1.0", END).strip()
        if not text:
            result_label.config(text="Please enter some text.")
            return

        url = "https://text-to-speach-english.p.rapidapi.com/makevoice"
        headers = {
            "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
            "x-rapidapi-host": "text-to-speach-english.p.rapidapi.com",
            "Content-Type": "application/json"
        }
        params = {"text": text}
        payload = {"key1": "value", "key2": "value"}

        try:
            response = requests.post(url, json=payload, headers=headers, params=params)
            if response.status_code != 200:
                result_label.config(text=f"Error: {response.status_code}")
                return

            with open("audio.mp3", "wb") as f:
                f.write(response.content)

            result_label.config(text="Audio saved as audio.mp3 and playing now...")
            os.system("start audio.mp3" if os.name == "nt" else "xdg-open audio.mp3")
        except Exception as e:
            result_label.config(text=f"Error: {e}")

    convert_btn = Button(win, text="Convert to Audio", font=("Arial", 14, "bold"),
                         bg="#09d8d8", fg="black", padx=20, pady=10,
                         relief="flat", cursor="hand2", command=convert_to_audio)
    convert_btn.place(relx=0.5, rely=0.55, anchor="center")

# === QR Code Generator Window === (your original code)
def generate_qr_window():
    win = Toplevel(root)
    win.title("QR Code Generator")
    win.geometry(f"{screen_width}x{screen_height}")
    win.configure(bg="white")

    bg_img = Image.open("Navy Blue Futuristic Technology Linktree Background (15).png")
    bg_img = bg_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(win, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(win, text="Generate QR Code", font=("Arial", 28, "bold"),
                  bg="white", fg="#5193B3")
    title.place(relx=0.5, y=80, anchor="center")

    input_label = Label(win, text="Enter text or link:", font=("Arial", 20, "bold"),
                        bg="white", fg="black")
    input_label.place(relx=0.5, rely=0.3, anchor="center")

    input_entry = Text(win, width=50, height=5, font=("Arial", 12))
    input_entry.place(relx=0.5, rely=0.4, anchor="center")

    result_label = Label(win, text="", font=("Arial", 12), bg="white", fg="green")
    result_label.place(relx=0.5, rely=0.6, anchor="center")

    qr_image_label = Label(win, bg="white")
    qr_image_label.place(relx=0.5, rely=0.65, anchor="center")

    def generate_qr():
        text = input_entry.get("1.0", END).strip()
        if not text:
            result_label.config(text="Please enter some text.")
            return

        url = "https://api.qrserver.com/v1/create-qr-code/"
        params = {
            "data": text,
            "size": "300x300"
        }

        try:
            response = requests.get(url, params=params)
            if response.status_code != 200:
                result_label.config(text=f"Error: {response.status_code}")
                return

            with open("QR.png", "wb") as f:
                f.write(response.content)

            qr_img = Image.open("QR.png")
            qr_img = qr_img.resize((200, 200), Image.Resampling.LANCZOS)
            qr_photo = ImageTk.PhotoImage(qr_img)
            qr_image_label.config(image=qr_photo)
            qr_image_label.image = qr_photo

        except Exception as e:
            result_label.config(text=f"Error: {e}")

    generate_btn = Button(win, text="Generate QR Code", font=("Arial", 14, "bold"),
                          bg="#00ffff", fg="black", padx=20, pady=10,
                          relief="flat", cursor="hand2", command=generate_qr)
    generate_btn.place(relx=0.5, rely=0.52, anchor="center")

# === Background Remover Window === (your original code)
def generate_bg_remover_window():
    win = Toplevel(root)
    win.title("Background Remover")
    win.geometry(f"{screen_width}x{screen_height}")
    win.configure(bg="white")
    
    win.grab_set()  # Focus on this window
    
    bg_img = Image.open("Navy Blue Futuristic Technology Linktree Background (12).png")
    bg_img = bg_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(win, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(win, text="Background Remover", font=("Arial", 28, "bold"),
                  bg="white", fg="#5193B3")
    title.place(relx=0.5, y=80, anchor="center")

    original_label = Label(win, text="Original Image", font=("Arial", 15, "bold"), bg="white")
    original_label.place(relx=0.3, rely=0.2, anchor="center")
    original_canvas = Label(win, bg="white")
    original_canvas.place(relx=0.3, rely=0.45, anchor="center")

    result_label = Label(win, text="Output Image", font=("Arial", 15, "bold"), bg="white")
    result_label.place(relx=0.7, rely=0.2, anchor="center")
    result_canvas = Label(win, bg="white")
    result_canvas.place(relx=0.7, rely=0.45, anchor="center")

    status_label = Label(win, text="", font=("Arial", 12), bg="white", fg="green")
    status_label.place(relx=0.5, rely=0.85, anchor="center")

    def choose_and_remove_bg():
        file_path = filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if not file_path:
            status_label.config(text="No image selected.")
            return

        try:
            img = Image.open(file_path)
            img_resized = img.resize((200, 200), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img_resized)
            original_canvas.config(image=img_tk)
            original_canvas.image = img_tk

            with open(file_path, 'rb') as image_file:
                image_data = image_file.read()

            boundary = "----011000010111000001101001"
            filename = os.path.basename(file_path)

            payload = (
                f"--{boundary}\r\n"
                f"Content-Disposition: form-data; name=\"image\"; filename=\"{filename}\"\r\n"
                f"Content-Type: image/jpeg\r\n\r\n"
            ).encode('utf-8') + image_data + f"\r\n--{boundary}--\r\n".encode('utf-8')

            headers = {
                "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
                "x-rapidapi-host": "background-removal4.p.rapidapi.com",
                "Content-Type": f"multipart/form-data; boundary={boundary}"
            }

            response = requests.post(
                "https://background-removal4.p.rapidapi.com/v1/results",
                data=payload,
                headers=headers
            )

            if response.status_code == 200:
                with open("bg_removed.png", "wb") as out_img:
                    out_img.write(response.content)

                output_img = Image.open("bg_removed.png").resize((200, 200), Image.Resampling.LANCZOS)
                output_tk = ImageTk.PhotoImage(output_img)
                result_canvas.config(image=output_tk)
                result_canvas.image = output_tk

                status_label.config(text="Background removed successfully!")
            else:
                status_label.config(text=f"Error: {response.status_code}")

        except Exception as e:
            status_label.config(text=f"Exception: {e}")

    action_btn = Button(win, text="Remove Background", font=("Arial", 14, "bold"),
                        bg="#00ffff", fg="black", padx=20, pady=10,
                        relief="flat", cursor="hand2", command=choose_and_remove_bg)
    action_btn.place(relx=0.5, rely=0.7, anchor="center")

# === NEW FEATURE: Plagiarism Checker Window ===
def generate_plagiarism_window():
    import requests  # Ensure it's imported if not already

    win = Toplevel(root)
    win.title("Plagiarism Checker")
    win.geometry(f"{screen_width}x{screen_height}")
    win.configure(bg="white")

    bg_img = Image.open("Navy Blue Futuristic Technology Linktree Background (12).png")
    bg_img = bg_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(win, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(win, text="Plagiarism Checker", font=("Arial", 28, "bold"),
                  bg="white", fg="#5193B3")
    title.place(relx=0.5, y=80, anchor="center")

    input_label = Label(win, text="Enter text to check plagiarism:", font=("Arial", 20, "bold"),
                        bg="white", fg="black")
    input_label.place(relx=0.5, rely=0.2, anchor="center")

    input_text = Text(win, width=70, height=10, font=("Arial", 14))
    input_text.place(relx=0.5, rely=0.4, anchor="center")

    result_label = Label(win, text="", font=("Arial", 14), bg="white", fg="green", justify="left")
    result_label.place(relx=0.5, rely=0.75, anchor="center")

    def check_plagiarism():
        text = input_text.get("1.0", END).strip()
        if not text:
            result_label.config(text="Please enter some text to check.")
            return

        url = "https://ai-content-identifier2.p.rapidapi.com/text"
        headers = {
            "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
            "x-rapidapi-host": "ai-content-identifier2.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        payload = {
            "text": text,
            "threshold": 10
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                result_label.config(text=f"API error: {response.status_code}")
                return

            data = response.json()
            percentage = data['data']['percentage']
            total_words = data['data']['stats']['totalWords']
            ai_words = data['data']['stats']['aiWords']
            human_words = data['data']['stats']['humanWords']

            result = (
                f"AI Detection Results:\n"
                f"AI Percentage: {percentage}%\n"
                f"Total Words: {total_words}\n"
                f"AI Words: {ai_words}\n"
                f"Human Words: {human_words}"
            )

            result_label.config(text=result)

        except requests.exceptions.RequestException as e:
            result_label.config(text=f"Request failed: {e}")

    check_btn = Button(win, text="Check Plagiarism", font=("Arial", 14, "bold"),
                       bg="#00ffff", fg="black", padx=20, pady=10,
                       relief="flat", cursor="hand2", command=check_plagiarism)
    check_btn.place(relx=0.5, rely=0.65, anchor="center")

# === NEW FEATURE: Image Colorizer Window ===
def generate_image_colorizer_window():
    win = Toplevel(root)
    win.title("Image Colorizer")
    win.geometry(f"{screen_width}x{screen_height}")
    win.configure(bg="white")
    win.grab_set()

    bg_img = Image.open("Navy Blue Futuristic Technology Linktree Background (12).png")
    bg_img = bg_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(win, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(win, text="Image Colorizer", font=("Arial", 28, "bold"),
                  bg="white", fg="#5193B3")
    title.place(relx=0.5, y=80, anchor="center")

    original_label = Label(win, text="Original Image", font=("Arial", 15, "bold"), bg="white")
    original_label.place(relx=0.3, rely=0.2, anchor="center")
    original_canvas = Label(win, bg="white")
    original_canvas.place(relx=0.3, rely=0.45, anchor="center")

    result_label = Label(win, text="Colorized Image", font=("Arial", 15, "bold"), bg="white")
    result_label.place(relx=0.7, rely=0.2, anchor="center")
    result_canvas = Label(win, bg="white")
    result_canvas.place(relx=0.7, rely=0.45, anchor="center")

    status_label = Label(win, text="", font=("Arial", 12), bg="white", fg="green")
    status_label.place(relx=0.5, rely=0.85, anchor="center")

    def choose_and_colorize():
        file_path = filedialog.askopenfilename(
            title="Select a Black & White Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if not file_path:
            status_label.config(text="No image selected.")
            return

        try:
            # Show original image in GUI
            img = Image.open(file_path)
            img_resized = img.resize((200, 200), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img_resized)
            original_canvas.config(image=img_tk)
            original_canvas.image = img_tk

            # Prepare API request
            url = "https://image-colorize.p.rapidapi.com/image/effects/colourize"
            headers = {
                "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
                "x-rapidapi-host": "image-colorize.p.rapidapi.com"
            }

            with open(file_path, "rb") as image_file:
                files = {"image": image_file}
                response = requests.post(url, headers=headers, files=files)

            if response.status_code != 200:
                status_label.config(text=f"API error: {response.status_code}")
                return

            result = response.json()
            base64_image = result.get("image")

            if not base64_image:
                status_label.config(text="Failed to get colorized image from API.")
                return

            # Decode the base64 image data
            image_data = base64.b64decode(base64_image)

            # Load decoded image into PIL and resize for display
            from io import BytesIO
            img_colorized = Image.open(BytesIO(image_data))
            img_colorized_resized = img_colorized.resize((200, 200), Image.Resampling.LANCZOS)
            img_color_tk = ImageTk.PhotoImage(img_colorized_resized)

            # Show colorized image in GUI
            result_canvas.config(image=img_color_tk)
            result_canvas.image = img_color_tk

            status_label.config(text="Image colorized successfully!")

        except Exception as e:
            status_label.config(text=f"Exception: {e}")

    action_btn = Button(win, text="Colorize Image", font=("Arial", 14, "bold"),
                        bg="#00ffff", fg="black", padx=20, pady=10,
                        relief="flat", cursor="hand2", command=choose_and_colorize)
    action_btn.place(relx=0.5, rely=0.7, anchor="center")

# === NEW FEATURE: YouTube Summarizer Window ===
def generate_youtube_summarizer_window():
    win = Toplevel(root)
    win.title("YouTube Video Summarizer")
    win.geometry(f"{screen_width}x{screen_height}")
    win.configure(bg="white")

    # Background image
    bg_img = Image.open("Navy Blue Futuristic Technology Linktree Background (12).png")
    bg_img = bg_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(win, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Title
    title = Label(win, text="YouTube Video Summarizer", font=("Arial", 28, "bold"),
                  bg="white", fg="#5193B3")
    title.place(relx=0.5, y=80, anchor="center")

    # URL Input
    url_label = Label(win, text="Enter YouTube Video URL:", font=("Arial", 20, "bold"),
                      bg="white", fg="black")
    url_label.place(relx=0.5, rely=0.2, anchor="center")

    url_entry = Entry(win, font=("Arial", 14), width=80)
    url_entry.place(relx=0.5, rely=0.3, anchor="center")

    # Summary Label
    summary_label = Label(win, text="Summary:", font=("Arial", 18, "bold"),
                          bg="white", fg="black")
    summary_label.place(relx=0.5, rely=0.4, anchor="center")

    # Summary Output Box
    summary_text = Text(win, width=90, height=15, font=("Arial", 12))
    summary_text.place(relx=0.5, rely=0.65, anchor="center")

    # Status Message
    status_label = Label(win, text="", font=("Arial", 12), bg="white", fg="green")
    status_label.place(relx=0.5, rely=0.9, anchor="center")

    # ---------------- Your Working Summarizer Logic ----------------
    def extract_video_id(url):
        parsed = urlparse(url)
        if "youtu.be" in parsed.netloc:
            return parsed.path.strip("/")
        if "youtube.com" in parsed.netloc:
            query = parse_qs(parsed.query)
            return query.get("v", [None])[0]
        return None

    def summarize_video():
        url = url_entry.get().strip()
        if not url:
            status_label.config(text="Please enter a YouTube video URL.", fg="red")
            return

        video_id = extract_video_id(url)
        if not video_id:
            status_label.config(text="Invalid YouTube URL.", fg="red")
            return

        api_url = "https://youtube-summarizer2.p.rapidapi.com/summarize"
        headers = {
            "x-rapidapi-key": "9ec364a01dmsh788ebdab04bbf6bp181b84jsn7d07939b6165",
            "x-rapidapi-host": "youtube-summarizer2.p.rapidapi.com"
        }
        querystring = {"id": video_id}

        try:
            response = requests.get(api_url, headers=headers, params=querystring)
            if response.status_code != 200:
                status_label.config(text=f"API error {response.status_code}", fg="red")
                return

            data = response.json()
            summary = data.get("summary", "No summary found.")

            summary_text.delete("1.0", END)
            summary_text.insert(END, summary)
            status_label.config(text="Summary generated successfully!", fg="green")

        except requests.exceptions.RequestException as e:
            status_label.config(text=f"Request failed: {e}", fg="red")

    # Button
    summarize_btn = Button(win, text="Summarize", font=("Arial", 14, "bold"),
                           bg="#00ffff", fg="black", padx=20, pady=10,
                           relief="flat", cursor="hand2", command=summarize_video)
    summarize_btn.place(relx=0.5, rely=0.8, anchor="center")

# ========== Main Root Window ==========

root = tk.Tk()
root.title("Cognitive AI Desk")

monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height

root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="white")

# === Background ===
bg_img = Image.open("Navy Blue Futuristic Technology Linktree Background (11) (2).png")
bg_img = bg_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# === Heading ===
heading = Label(root, text="Cognitive AI Desk", font=("Arial", 36, "bold"),
                bg="white", fg="#5193B3")
heading.place(relx=0.5, y=80, anchor="center")

# === Buttons Frame ===
button_frame = Frame(root, bg="white")
button_frame.place(relx=0.5, rely=0.5, anchor="center")

# === Button Style Settings ===
button_style = {
    "font": ("Arial", 14, "bold"),
    "bg": "#001F3F",          # Navy blue
    "fg": "white",
    "width": 25,
    "height": 3,
    "bd": 0,
    "relief": "flat",
    "cursor": "hand2",
    "activebackground": "#003366",
    "activeforeground": "white"
}

# === Button Grid Arrangement ===
button_texts = [
    ("Plagiarism Checker", 0, 0),
    ("Background Remover", 0, 1),
    ("QR Code Generator", 1, 0),
    ("Audio Generator", 1, 1),
    ("Image Colorizer", 2, 0),
    ("Youtube Summarizer", 2, 1)
]

for text, row, col in button_texts:
    if text == "Audio Generator":
        command = generate_audio_window
    elif text == "QR Code Generator":
        command = generate_qr_window
    elif text == "Background Remover":
        command = generate_bg_remover_window
    elif text == "Plagiarism Checker":
        command = generate_plagiarism_window
    elif text == "Image Colorizer":
        command = generate_image_colorizer_window
    elif text == "Youtube Summarizer":
        command = generate_youtube_summarizer_window
    else:
        command = lambda t=text: print(f"{t} clicked")

    btn = Button(button_frame, text=text, command=command, **button_style)
    btn.grid(row=row, column=col, padx=40, pady=20)

    # Hover Effects
    def on_enter(e, b=btn): b.config(bg="#003366")
    def on_leave(e, b=btn): b.config(bg="#001F3F")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()
