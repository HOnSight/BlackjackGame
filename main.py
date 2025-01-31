import tkinter as tk
from home_page import create_home_page
from game_page import create_game_page

# Root window
root = tk.Tk()
root.title("Blackjack App")
root.geometry("800x600")

# Laad de Home-pagina als eerste
create_home_page(root)

root.mainloop()