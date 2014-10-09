import Tkinter as tk
import cv2
from PIL import Image, ImageTk

citac = 0

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

def konec(x):
    root.destroy()

root = tk.Tk()
root.bind('<Escape>', konec)
lmain = tk.Label(root)
lmain.pack()

def show_frame():
    global citac
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    if citac == 20:
        cv2.imwrite("obrazek.png",cv2image)
        konec(0)
    citac = citac + 1
    lmain.after(10, show_frame)

show_frame()
root.mainloop()