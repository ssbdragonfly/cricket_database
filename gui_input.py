import tkinter as tk
from tkinter import simpledialog

def get_shot_type(over, ball):
    root = tk.Tk()
    root.withdraw()
    prompt = f"Enter the type of shot for Over: {over}, Ball: {ball}"
    shot_type = simpledialog.askstring("Input", prompt)
    root.destroy()
    return shot_type
