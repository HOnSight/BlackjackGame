import tkinter as tk
from tkinter import PhotoImage
from home_page import create_home_page

# Root window
root = tk.Tk()
root.title("Blackjack")
root.geometry("800x600")

# Maak een Canvas widget aan om de afbeelding als achtergrond te plaatsen
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

# Laad de afbeelding en zet deze op het Canvas
background_image = PhotoImage(file="Table mat.jpg")  
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Laad de Home-pagina als eerste
create_home_page(root)

root.mainloop()
