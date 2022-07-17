import tkinter as tk
from tkinter import filedialog

def file_select():
    root=tk.Tk()
    root.withdraw()

    file_path=filedialog.askopenfilename()
    print(file_path)
 
    return file_path