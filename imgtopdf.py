import img2pdf
import tkinter as tk
from tkinter import ttk, filedialog
import os

root = tk.Tk()
root.wm_title("IMG2PDF")
root.geometry("341x192")

heading = ttk.Label(root, text="IMG2PDF", font=("Segoe UI", 24))
heading.pack()

in_path = None
out_path = None

def select_jpg():
    global in_path
    in_path = filedialog.askopenfilename(
        parent=None,
        title="Select JPG File",
        filetypes=(("JPG Images", "*.jpg"), ("All files", "*.*"))
    )
    if in_path:
        info_lbl.config(text="Added JPG file.")
    return in_path

def output_jpg():
    global out_path
    out_path = filedialog.asksaveasfilename(
        parent=None,
        title="Save PDF File",
        defaultextension=".pdf",
        filetypes=(("PDF Files", "*.pdf"), ("All files", "*.*"))
    )
    if not in_path or not out_path:
        info_lbl.config(text="Please select a JPG file and output location.")
        return
    
    filepath = in_path.replace("/", "\\")
    try:
        if os.path.isfile(filepath) and filepath.endswith(".jpg"):
            with open(out_path, "wb") as f:
                f.write(img2pdf.convert(filepath))
            info_lbl.config(text="PDF saved successfully!")
        else:
            info_lbl.config(text="An error occurred. Please add a JPG file.")
    except Exception as e:
        info_lbl.config(text=f"Error: {str(e)}")

input_btn = ttk.Button(root, text="Open JPG File", command=select_jpg)
input_btn.pack()

output_btn = ttk.Button(root, text="Save PDF File", command=output_jpg)
output_btn.pack()

info_lbl = ttk.Label(root, text="", font=("Segoe UI", 11))
info_lbl.pack()

if __name__ == "__main__":
    root.mainloop()