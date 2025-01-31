import tkinter as tk
from PIL import Image, ImageTk
from rules import create_rules_page  # Zorg ervoor dat de rules-pagina correct wordt aangeroepen

def create_home_page(root):
    home_frame = tk.Frame(root, bg="darkgreen")

    # Logo
    try:
        logo_image = Image.open("assets/logo.png").resize((200, 200))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(home_frame, image=logo_photo, bg="darkgreen")
        logo_label.image = logo_photo  # Bewaar referentie
        logo_label.pack(pady=20)
    except FileNotFoundError:
        logo_label = tk.Label(home_frame, text="Logo hier", font=("Arial", 24), bg="darkgreen")
        logo_label.pack(pady=20)

    # Titel
    title_label = tk.Label(home_frame, text="Blackjack!", font=("Arial", 24), bg="darkgreen")
    title_label.pack(pady=10)

    # Start Game knop
    start_button = tk.Button(home_frame, text="Start Game", command=lambda: show_game_page(root, home_frame), bg="white", font=("Arial", 16))
    start_button.pack(pady=20)

    # Knop naar de spelregels pagina
    rules_button = tk.Button(home_frame, text="Bekijk Spelregels", command=lambda: show_rules_page(root, home_frame), bg="white", font=("Arial", 16))
    rules_button.pack(pady=20)

    home_frame.pack(fill="both", expand=True)

def show_game_page(root, home_frame):
    home_frame.pack_forget()  # Verberg de Home-pagina
    from game_page import create_game_page
    create_game_page(root)  # Laad de Game-pagina

def show_rules_page(root, home_frame):
    home_frame.pack_forget()  # Verberg de Home-pagina
    create_rules_page(root)  # Laad de spelregels-pagina
