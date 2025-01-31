import tkinter as tk
from tkinter import messagebox
from utils import load_card_images, deal_card, calculate_score

def show_home_page(root, game_frame):
    """Keert terug naar de Home-pagina"""
    game_frame.pack_forget()  # Verberg de Game-pagina
    from home_page import create_home_page
    create_home_page(root)  # Laad de Home-pagina

def hit(game_frame):
    """Handles the 'Hit' action by adding a card to the player's hand."""
    player_hand = game_frame.player_hand  # Ophalen uit game_frame
    card = deal_card(player_hand)  # ✅ Nu krijgt deal_card() het juiste argument
    score = calculate_score(player_hand)
    if score > 21:
        messagebox.showinfo("Game Over", "You busted! Dealer wins.")

def stand():
    """Handles the 'Stand' action by ending the player's turn."""
    messagebox.showinfo("Stand", "You chose to stand. Dealer's turn!")

def create_game_page(root):
    game_frame = tk.Frame(root, bg="green")
    game_frame.player_hand = []  # ✅ Slaat de hand op als een attribuut van game_frame

    # Frames for cards and buttons
    dealer_frame = tk.Frame(game_frame, bg="green")
    dealer_frame.pack(pady=10)

    player_frame = tk.Frame(game_frame, bg="green")
    player_frame.pack(pady=10)

    # Buttons
    button_frame = tk.Frame(game_frame, bg="green")
    button_frame.pack(pady=20)

    hit_button = tk.Button(button_frame, text="Hit", command=lambda: hit(game_frame), bg="white")
    hit_button.grid(row=0, column=1, padx=5)

    stand_button = tk.Button(button_frame, text="Stand", command=stand, bg="white")
    stand_button.grid(row=0, column=2, padx=5)

    leave_button = tk.Button(button_frame, text="Leave Table", command=lambda: show_home_page(root, game_frame), bg="white")
    leave_button.grid(row=0, column=3, padx=5)

    game_frame.pack(fill="both", expand=True)
