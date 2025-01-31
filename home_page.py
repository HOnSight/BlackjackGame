import tkinter as tk
from tkinter import ttk

def create_home_page(root, show_game, show_rules):
    """Creëert de homepagina met knoppen voor Play en Rules."""
    home_frame = tk.Frame(root, bg="darkgreen")
    home_frame.pack(fill="both", expand=True)

    title_label = tk.Label(home_frame, text="Welcome to Blackjack!", font=("Arial", 24), bg="darkgreen", fg="white")
    title_label.pack(pady=50)

    play_button = ttk.Button(home_frame, text="Play Game", command=lambda: show_game(home_frame))
    play_button.pack(pady=10)

    rules_button = ttk.Button(home_frame, text="Rules", command=lambda: show_rules(home_frame))
    rules_button.pack(pady=10)

    return home_frame
