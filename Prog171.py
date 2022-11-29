import tkinter as tk
from PIL import Image
'''
win = Tk()
win.title("SKSCricInfo")
win.geometry("500x500")
filename = PhotoImage(file="C:\\Users\\Shivakumar\\Desktop\\cricket.png")
background_label = Label(win, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
win.mainloop()'''
root = tk.Tk()
file = "khaby-lame.gif"

info = Image.open(file)
frames = info.n_frames
print(frames)

im = [tk.PhotoImage(file=file,format=f'gif -index{i}') for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]
    gif_label.configure(image=im2)

    count+=1

    if count == frames:
        count = 0

    anim = root.after(50,lambda :animation(count))

def stop_animation():
    global anim
    root.after_cancel(anim)
gif_label = tk.Label(image="")
gif_label.pack()

start = tk.Button(text = "start",command=lambda :animation(count))
start.pack()

stop = tk.Button(text="stop",command = stop_animation)
stop.pack()

root.mainloop()