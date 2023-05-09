from tkinter import Tk, Label, Button
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x500")
root.title("Background Image Example")

# Load and resize the image
image = Image.open(r"C:\Users\VEDANT SAXENA\Dropbox\My PC (LAPTOP-QJ4EJ2DM)\Pictures\Movie art\947accadfc196438ae3e3c8d153602a3.jpg")
image = image.resize((500, 500))
background_image = ImageTk.PhotoImage(image)

# Create a label for the background image
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add other widgets on top of the background
button = Button(root, text="Click Me")
button.place(x=200, y=200)

root.mainloop()
