# root = Tk()
# root.title("<GVBH")
# root.geometry("350x200")
# ibl = Label(root, text = "Фурри любишь?")
# ibl.grid()
#
# def clicked():
#     if btn.cget("text") == "Да":
#         btn.configure(text="Нет")
#     else:
#         btn.configure(text="Да")
#
# btn=Button(root, text="Да",fg="red", command=clicked)
# btn.grid(column=0, row=1)
#
# def clicked1():
#     if btn1.cget("text") == "Нет":
#         btn1.configure(text="Да")
#     else:
#         btn1.configure(text="Нет")
# btn1=Button(root, text="Нет",fg="red", command=clicked1)
# btn1.grid(column=0, row=2)
# root.mainloop()

#root = Tk()
#root.title("Test")
#root.geometry("1000x600")

#img = PhotoImage(file="Снимок экрана 2026-09-07 110705.png")
#photo = Label(root, image=img)
#img.geometry("1000x600")
#photo.pack()


#root.mainloop()

# root = Tk()
# root.geometry("300x300")
#
# def open_window():
#     new_window = Toplevel(root)
#     new_window.title("?")
#     new_window.geometry("300x200")
#
#     Label(new_window, text="новое").pack()
#
# btn = Button(root, text="open", command=open_window)
# btn.pack()
#
# root.mainloop()

# root = Tk()
# root.geometry("300x200+0+100")
# x=0
# y=0
# speed = 200
# def move():
#     global x,y,speed
#
#     x+= speed
#     y+= speed
#
#     if x <= 0 or x >= root.winfo_screenwidth() - 300:
#         speed = -speed
#
#     root.geometry(f"300x200+{x}+{y}")
#
#     root.after(10, move)
#
# move()
# root.mainloop()
