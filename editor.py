import tkinter
from tkinter import ttk
from tkinter import filedialog
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
notepad_text_box = tkinter.Text(root, height=28)
notepad_text_box.grid(row=1, column=1, columnspan=3)


current_file = ""

def open_document(file_path=None):
    global current_file
    if file_path is None: 
        current_file = filedialog.askopenfilename()
    if file_path: 
        current_file = file_path
    with open(current_file) as fopen_file: 
        text_to_insert = fopen_file.read()
    notepad_text_box.delete("1.0", "end")
    notepad_text_box.insert("1.0",  text_to_insert)
    file_without_path = os.path.basename(current_file)
    root.title(file_without_path + " in Notepad--")


def save_document():
    if(current_file != ""): 
        text_to_save = notepad_text_box.get("1.0", "end")
        with open(current_file, "w") as kopen_file: 
            kopen_file.write(text_to_save)

    
def new_document():
    new_document_name = filedialog.asksaveasfilename(defaultextension=".nptxt", filetypes=[("Notepad-- Text files", "*.nptxt"), ("All files", "*.*")])
    open(new_document_name, "x")
    open_document(new_document_name)

def placeholder_one():
    print("placeholder_one")
    
def placeholder_two():
    print("placeholder_two")
    
def exit_function():
    root.quit()
    
open_button = ttk.Button(root, text = "Open", command = open_document)
save_button = ttk.Button(root, text = "Save", command = save_document)
new_button  = ttk.Button(root, text = "New", command = new_document)
placeholder_button_one  = ttk.Button(root, text = "placeholder_one", command = placeholder_one)
placeholder_button_two  = ttk.Button(root, text = "placeholder_two", command = placeholder_two)
exit_button  = ttk.Button(root, text = "Exit", command = exit_function)

root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

open_button.grid(row=2, column=1)
save_button.grid(row=2,column=2)
new_button.grid(row=2,column=3)
placeholder_button_one.grid(row=3,column=1)
placeholder_button_two.grid(row=3,column=2)
exit_button.grid(row=3,column=3)

if len(sys.argv) > 1:
    open_document(sys.argv[1])

root.mainloop()

