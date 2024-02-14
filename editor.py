import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import Tk
import sys
import os

root = tkinter.Tk()

window_width = 380
window_height = 503

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.resizable(False, False)

root.title("Notepad--")

script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "icon.ico")
root.iconbitmap(icon_path)

def update_title(event): 
    print("update_title called")
    if(root.title()[0:1] != "*"): 
        root.title("*" + root.title())
        print("title updated")

current_file = ""

notepad_text_box = tkinter.Text(root, height=28)
notepad_text_box.grid(row=1, column=1, columnspan=3)
notepad_text_box.bind("<KeyRelease>", update_title)

def open_document(file_path=None):
    global current_file
    if file_path is None: 
        current_file = filedialog.askopenfilename()
    if file_path: 
        current_file = file_path
    with open(current_file) as fopen_file: 
        text_to_insert = fopen_file.read()
    notepad_text_box.replace("1.0",  "end", text_to_insert)
    file_without_path = os.path.basename(current_file)
    if(root.title()[:1] == "*"): 
       root.title(root.title()[1:len(root.title())])

    root.title(file_without_path + " in Notepad--")

def save_as():
    global current_file
    current_file = ""
    save_document()

def save_document():
    global current_file
    if(current_file == ""): 
        current_file = filedialog.asksaveasfilename(defaultextension=".nptxt", filetypes=[("Notepad-- Text files", "*.nptxt"), ("All files", "*.*")])
    text_to_save = notepad_text_box.get("1.0", "end")
    with open(current_file, "w") as kopen_file: 
        kopen_file.write(text_to_save)
    open_document(current_file)
    
def new_document():
    new_document_name = filedialog.asksaveasfilename(defaultextension=".nptxt", filetypes=[("Notepad-- Text files", "*.nptxt"), ("All files", "*.*")])
    open(new_document_name, "x")
    open_document(new_document_name)

def copy_to_clipboard():
    copier = Tk()
    copier.withdraw()
    copier.clipboard_clear()
    copier.clipboard_append(notepad_text_box.get("1.0", "end-1c"))
    copier.update()
    copier.destroy()
    
def exit_function():
    root.quit()
    
open_button = ttk.Button(root, text = "Open", command = open_document)
save_button = ttk.Button(root, text = "Save", command = save_document)
new_button  = ttk.Button(root, text = "New", command = new_document)
copy_button  = ttk.Button(root, text = "Copy", command = copy_to_clipboard)
save_as_button  = ttk.Button(root, text = "Save As", command = save_as)
exit_button  = ttk.Button(root, text = "Exit", command = exit_function)

root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

open_button.grid(row=2, column=1)
save_button.grid(row=2,column=2)
new_button.grid(row=2,column=3)
copy_button.grid(row=3,column=1)
save_as_button.grid(row=3,column=2)
exit_button.grid(row=3,column=3)

if len(sys.argv) > 1:
    open_document(sys.argv[1])

root.mainloop()

