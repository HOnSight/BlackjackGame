import tkinter as tk
from tkinter import PhotoImage
from home_page import create_home_page

# Root window   
root = tk.Tk()
root.title("Blackjack")
root.geometry("800x600")


# Laad de Home-pagina als eerste
create_home_page(root)

root.mainloop()
