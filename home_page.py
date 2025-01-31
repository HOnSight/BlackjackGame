import tkinter as tk
from PIL import Image, ImageTk

def create_home_page(root):
    home_frame = tk.Frame(root, bg="lightblue")

    # Logo
    try:
        logo_image = Image.open("assets/logo.png").resize((200, 200))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(home_frame, image=logo_photo, bg="lightblue")
        logo_label.image = logo_photo  # Bewaar een referentie om garbage collection te voorkomen
        logo_label.pack(pady=20)
    except FileNotFoundError:
        logo_label = tk.Label(home_frame, text="Logo hier", font=("Arial", 24), bg="lightblue")
        logo_label.pack(pady=20)

    # Titel
    title_label = tk.Label(home_frame, text="Welkom bij Blackjack!", font=("Arial", 24), bg="lightblue")
    title_label.pack(pady=10)

    # Start Game knop
    start_button = tk.Button(home_frame, text="Start Game", command=lambda: show_game_page(root, home_frame), bg="white", font=("Arial", 16))
    start_button.pack(pady=20)

    # Spelinformatie
    info_label = tk.Label(home_frame, text="Druk op 'Start Game' om te beginnen.", font=("Arial", 14), bg="lightblue")
    info_label.pack(pady=10)

    home_frame.pack(fill="both", expand=True)

def show_game_page(root, home_frame):
    home_frame.pack_forget()  # Verberg de Home-pagina
    from game_page import create_game_page
    create_game_page(root)  # Laad de Game-pagina