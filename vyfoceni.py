from __future__ import print_function
import Tkinter as tk
import cv2
from PIL import Image, ImageTk

citac = 0

width, height = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
cap.set(12, 1)
cap.set(11, 0)
print(cap.get(3),cap.get(4))

def konec(x):
    root.destroy()

root = tk.Tk()
root.bind('<Escape>', konec)
lmain = tk.Label(root)
lmain.pack()

def show_frame():
    global citac
    citac = citac + 1
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    if citac == 200:
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("obrazek.png", frame)
        print("ahoj")
        konec(0)
    lmain.after(10, show_frame)

show_frame()
root.mainloop()