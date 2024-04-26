import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

# Function to convert image to sketch
def convert_to_sketch(image, kernel_size=(5, 5), sigma=0.5, amount=1.0):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, kernel_size, sigma)
    img_blend = cv2.divide(img_gray, img_blur, scale=256)
    img_sketch = cv2.multiply(amount, img_blend)
    return cv2.cvtColor(img_sketch.astype('uint8'), cv2.COLOR_GRAY2BGR)

# Function to handle image upload
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        sketch = convert_to_sketch(image)
        preview_image(sketch)

# Function to preview the converted sketch
def preview_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (400, 400))
    photo = tk.PhotoImage(data=image)
    preview_label.configure(image=photo)
    preview_label.image = photo

# Function to save the converted sketch
def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if file_path:
        cv2.imwrite(file_path, cv2.cvtColor(preview_label.image, cv2.COLOR_RGB2BGR))

# GUI Setup
root = tk.Tk()
root.title("Image to Sketch Converter")

# Create GUI elements
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

preview_label = tk.Label(root)
preview_label.pack()

save_button = tk.Button(root, text="Save Sketch", command=save_image)
save_button.pack(pady=10)

root.mainloop()