import tkinter as tk
from tkinter import ttk

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="darkgreen")
        self.controller = controller

        # Titel
        title_label = tk.Label(self, text="Blackjack Game", font=("Arial", 32, "bold"), bg="darkgreen", fg="white")
        title_label.pack(pady=50)

        # Play-knop
        play_button = ttk.Button(self, text="Play", command=lambda: controller.show_frame("GameInterface"))
        play_button.pack(pady=20)

        # Rules-knop
        rules_button = ttk.Button(self, text="Rules", command=lambda: controller.show_frame("RulesPage"))
        rules_button.pack(pady=10)
