import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Viewer")
root.geometry("600x500")

image = None
photo = None

def open_image():
    global image, photo
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                   ("All files", "*.*")]
    )
    
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((550, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        info.config(text=f"Image: {file_path.split('/')[-1]}")

tk.Button(root, text="Open Image", command=open_image,
         width=20, bg='green', fg='white', font=("Arial", 12)).pack(pady=10)

label = tk.Label(root, bg='gray', height=20)
label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

info = tk.Label(root, text="No image loaded", bg='white')
info.pack(fill=tk.X, padx=10, pady=5)

root.mainloop()
