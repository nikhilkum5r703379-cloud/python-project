# import tkinter for creating GUT apps.
import tkinter as tk
from tkinter import filedialog, messagebox

root=tk.Tk()
root.title("Nikhil Text Editor")
root.geometry("900x800")

# creat text area
text= tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetice",10)
)

text.pack(expand=True,fill=tk.BOTH)

def new_file():
    text.delete(1.0, tk.END)


def open_file():
    file_path= filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        with open(file_path, "r")as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END, file.read())


def save_file():

    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w")as file:
            file.write(text.get(1.0, tk.END))


    messagebox.showinfo("Info","File saved successfully")


manu=tk.Menu(root)
root.config(menu=manu)
file_menu = tk.Menu(manu)


manu.add_cascade(label="File", menu=file_menu)


file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
