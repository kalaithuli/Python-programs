from tkinter import *
from PIL import ImageTk, Image
import time
from itertools import count, cycle
from tkinter import messagebox
global root
def win():
    pass
class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


root = Toplevel()
global lbl
lbl = ImageLabel(root)
lbl.pack()
lbl.load('khaby-lame-gif-3.gif')
lbl1 = Button(root, text="SIGN IN", width=10, font=("bold", 15), fg='pink', command=win)
lbl1.config(bg='black')
lbl1.place(x=340, y=200)  # 348 200
root.mainloop()

