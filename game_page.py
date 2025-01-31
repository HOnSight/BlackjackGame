import tkinter as tk
from tkinter import messagebox
from utils import load_card_images, deal_card, calculate_score

def create_game_page(root):
    game_frame = tk.Frame(root, bg="green")

    # Frames voor kaarten en knoppen
    dealer_frame = tk.Frame(game_frame, bg="green")
    dealer_frame.pack(pady=10)

    player_frame = tk.Frame(game_frame, bg="green")
    player_frame.pack(pady=10)

    # Knoppen
    button_frame = tk.Frame(game_frame, bg="green")
    button_frame.pack(pady=20)

    hit_button = tk.Button(button_frame, text="Hit", command=lambda: hit(player_hand), bg="white")
    hit_button.grid(row=0, column=1, padx=5)

    stand_button = tk.Button(button_frame, text="Stand", command=stand, bg="white")
    stand_button.grid(row=0, column=2, padx=5)

    leave_button = tk.Button(button_frame, text="Leave Table", command=lambda: show_home_page(root, game_frame), bg="white")
    leave_button.grid(row=0, column=3, padx=5)

    game_frame.pack(fill="both", expand=True)

def show_home_page(root, game_frame):
    game_frame.pack_forget()  # Verberg de Game-pagina
    from home_page import create_home_page
    create_home_page(root)  # Laad de Home-pagina