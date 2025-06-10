import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def animate_hand():
    global hand_y, direction
    hand_y += direction
    if hand_y > original_y + 10 or hand_y < original_y - 10:
        direction *= -1
    hand_label.place(x=hand_x, y=hand_y)
    root.after(100, animate_hand)  # Move every 100 ms

root = tk.Tk()
root.title("Cogetive AI Desk")
root.geometry("1440x960")
root.configure(bg="white")

# ==== Static Background ====
bg_img = Image.open("Navy Blue Futuristic Technology Linktree Background (8).png")
bg_img = bg_img.resize((1440, 960), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ==== Moving Hand ====
hand_img = Image.open("hand.png")  # Transparent hand image
hand_img = hand_img.resize((250, 250), Image.Resampling.LANCZOS)
hand_photo = ImageTk.PhotoImage(hand_img)

hand_x = 1000
original_y = 200
hand_y = original_y
direction = 2

hand_label = Label(root, image=hand_photo, bg="white", bd=0)
hand_label.place(x=hand_x, y=hand_y)

# Start animation
animate_hand()

root.mainloop()
