import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from PyPDF2 import PdfReader
import itertools
import os
import pygame
from PIL import Image, ImageTk

# Initialize pygame mixer for sound
pygame.mixer.init()
def play_sound():
    try:
        pygame.mixer.music.load("success.mp3")
        pygame.mixer.music.play()
    except Exception as e:
        print("Sound error:", e)

# Main GUI setup
root = tk.Tk()
root.title("PDF Password Cracker PRO")
root.geometry("600x500")

# Load background image
try:
    bg_image = Image.open("background4.jpg")
    bg_photo = ImageTk.PhotoImage(bg_image.resize((600, 500)))
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    pass

# Output log area
output_text = ScrolledText(root, height=10, bg="black", fg="lime")
output_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Progress bar
progress_var = tk.DoubleVar()
progress_bar = tk.ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill=tk.X, padx=10, pady=5)

# Theme toggle
is_dark = False
def toggle_theme():
    global is_dark
    if is_dark:
        root.configure(bg="white")
        output_text.configure(bg="white", fg="black")
    else:
        root.configure(bg="black")
        output_text.configure(bg="black", fg="lime")
    is_dark = not is_dark

# PDF selection
pdf_path_var = tk.StringVar()
def browse_pdf():
    path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_path_var.set(path)

def crack_password(pdf_path, max_length):
    found = False
    try:
        reader = PdfReader(pdf_path)
        for length in range(1, max_length+1):
            for pwd_tuple in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=length):
                pwd = ''.join(pwd_tuple)
                output_text.insert(tk.END, f"Trying: {pwd}\n")
                output_text.see(tk.END)
                root.update()
                try:
                    if reader.decrypt(pwd):
                        found = True
                        output_text.insert(tk.END, f"[+] Password Found: {pwd}\n")
                        play_sound()
                        return
                except:
                    continue
                progress = ((length - 1) * (26 ** length)) / (26 ** max_length) * 100
                progress_var.set(progress)
                root.update_idletasks()
        if not found:
            output_text.insert(tk.END, "[-] Password Not Found\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# UI Widgets
pdf_entry = tk.Entry(root, textvariable=pdf_path_var, width=50)
pdf_entry.pack(pady=5)
browse_btn = tk.Button(root, text="Browse PDF", command=browse_pdf)
browse_btn.pack(pady=5)

length_label = tk.Label(root, text="Max Length (for Brute-force):")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "3")
length_entry.pack(pady=5)

def start_cracking():
    path = pdf_path_var.get()
    if not os.path.exists(path):
        messagebox.showwarning("No file", "Please select a valid PDF.")
        return
    try:
        max_length = int(length_entry.get())
    except:
        messagebox.showwarning("Invalid input", "Enter valid number for max length")
        return
    output_text.delete('1.0', tk.END)
    crack_password(path, max_length)

start_btn = tk.Button(root, text="Start Cracking", command=start_cracking, bg="green", fg="white")
start_btn.pack(pady=5)

toggle_btn = tk.Button(root, text="Toggle Theme", command=toggle_theme)
toggle_btn.pack(pady=5)

root.mainloop()