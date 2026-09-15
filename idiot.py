from tkinter import *
import random
import pygame
from PIL import Image, ImageTk
import threading

root = Tk()
root.geometry("300x300")

pygame.mixer.init()

# -gif-------------------------------------------------------------------------------
gif = Image.open("you-are-an-idiot.gif")
gw = gif.width
gh = gif.height - 100

frames = []

for i in range(gif.n_frames):
    gif.seek(i)
    frame = gif.convert("RGBA").copy()
    frames.append(ImageTk.PhotoImage(frame))

# -Okna----------------------------------------------------------------------------
windows = []

def open_window():
    window = Toplevel(root)

    x = random.randint(0, root.winfo_screenwidth() - gw)
    y = random.randint(0, root.winfo_screenheight() - gh)

    window.geometry(f"{gw}x{gh}+{x}+{y}")
    label = Label(window, image=frames[0], borderwidth=0)
    label.pack()
    animate_gif(window, label)

    dx = random.choice([-10, 10])
    dy = random.choice([-10, 10])

    move_window(window, x,y,dx,dy)

    windows.append(window)

def animate_gif(window, label, frame=0):
    if not window.winfo_exists():
        return

    label.config(image=frames[frame])
    frame = (frame + 1) % len(frames)
    window.after(50, animate_gif, window, label, frame)

def move_window(window, x, y, dx, dy):
    if not window.winfo_exists():
        return
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x += dx
    y += dy
    if  x + gw >= screen_width:
        x = screen_width - gw
        dx = -abs(dx)
    elif  x <= 0:
        x = 0
        dx = abs(dx)
    if y + gh >= screen_height:
        y = screen_height - gh
        dy = -abs(dy)
    elif y <= 0:
        y = 0
        dy = abs(dy)
    window.geometry(f"{gw}x{gh}+{x}+{y}")
    window.after(10, move_window, window, x, y, dx, dy)
#-start------------------------------------------------------------------------
def start():
    pygame.mixer.music.load("you-are-an-idiot.mp3")
    pygame.mixer.music.play(-1)
    open_window()
    root.after(500, create_one_win_loop)

def create_one_win_loop():
    open_window()
    root.after(500, create_one_win_loop)


Button(root, text="ЖМИИИИ", command=start).pack(pady=50)
root.mainloop()







