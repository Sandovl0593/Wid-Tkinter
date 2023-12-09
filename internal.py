import tkinter as tk
from tkinter.constants import *

window = tk.Tk()
window.config(width=300, height=200)

frame = tk.Frame(window, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

message = tk.Label(frame, text = "")
message.pack(fill=CENTER, expand=1)

def message_show(string: str):
    message.config(text= string)

def message_close():
    message.config(text = "")