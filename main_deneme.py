import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox


window = tk.Tk()

# window settings
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()
window_width = 400
window_height = 600
x = int((SCREEN_WIDTH / 2) - (window_width / 2))
y = int((SCREEN_HEIGHT / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.resizable(False, False)

# Variables
style = ("Calibri", 14, "normal")
widget_width = 30
img = ImageTk.PhotoImage(Image.open("pngwing.com.png").resize((150, 150)))


# Defines
def save_and_encrypt():
    if (widgets.title_entry.get() == "" or widgets.secret_entry.get("1.0", 'end-1c') == "" or widgets.master_key_entry.get() == ""):
        messagebox.showerror("Değerleri Düzgün Giriniz!", "Lütfen değerleri düzgün giriniz.")
    else:
        text_title = widgets.title_entry.get()
        text_content = widgets.secret_entry.get("1.0", 'end-1c')
        text_master_key = widgets.master_key_entry.get()
        with open("my_secret.txt", mode='a') as f:
            pass



# Image Placement
def place_image():
    label = tk.Label(window)
    label.config(image = img)
    label.pack()
    print("sa")


class Widgets():
    # Set Widgets
    title_entry = tk.Entry()
    secret_entry = tk.Text()
    master_key_entry = tk.Entry()

    title_label = tk.Label(text="Enter your title", font=style)
    secret_label = tk.Label(text="Enter your secret", font=style)
    master_key_label = tk.Label(text="Enter master key", font=style)

    def __init__(self):
        # class initilaze
        place_image()
        self.title_entry.config(font=style, width=widget_width)
        self.secret_entry.config(font=style, height=5, width=widget_width)
        self.master_key_entry.config(font=style, width=widget_width)

        self.save_encrypt_button = tk.Button(text="Save & Encrypt", font=style, width=widget_width, bg="#7f8fa6", fg="#f5f6fa", command=save_and_encrypt)
        self.decrypt_button = tk.Button(text="Decrypt", font=style, width=widget_width, bg="#7f8fa6", fg="#f5f6fa")

        self.title_label.pack()
        self.title_entry.pack(pady=(0, 20))

        self.secret_label.pack()
        self.secret_entry.pack(pady=(0, 20))

        self.master_key_label.pack()
        self.master_key_entry.pack(pady=(0, 20))

        self.save_encrypt_button.pack(pady=(0, 20))
        self.decrypt_button.pack()

widgets = Widgets()


window.mainloop()