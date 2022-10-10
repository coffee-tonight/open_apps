import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
files = []
# <_io.TextIOWrapper name='F:/documents/GTA San Andreas User Files/GTASAsf1.b' mode='r' encoding='cp1252'>
def opendir():
    filedir = filedialog.askopenfile(title="SelectFiles", initialdir="/",
                                     filetypes=(("executable", "*.*"), ("all files", "*.*")))
    files.append(str(filedir).replace("<_io.TextIOWrapper name='", "").replace("' mode='r' encoding='cp1252'>", ""))
    filedire = (str(filedir).replace("<_io.TextIOWrapper name='", "").replace("' mode='r' encoding='cp1252'>", ""))
    print(filedire)
    
    label = tk.Label(frame, text=filedire)
    label.pack()

def start():
    for file in files:
        os.startfile(file)

canvas = tk.Canvas(root, height=200, width=200, bg="#202020")
canvas.pack()

frame = tk.Frame(root, bg="red")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=.1)

openfile = tk.Button(root, text="Click", padx=10, pady=10, fg="black", bg="#123456", command=opendir)
openfile.pack()

send = tk.Button(root, bg="#213243", padx=10, pady=10, text="click2", fg="white", command=start)
send.pack()

root.mainloop()
