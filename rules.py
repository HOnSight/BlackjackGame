import tkinter as tk
from tkinter import ttk

class RulesPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="darkgreen")
        self.controller = controller

        title_label = tk.Label(self, text="Blackjack Rules", font=("Arial", 24, "bold"), bg="darkgreen", fg="white")
        title_label.pack(pady=20)

        rules_text = """1. Het doel is om 21 punten te halen zonder eroverheen te gaan.\n
2. Plaatjes tellen als 10, een Aas telt als 1 of 11.\n
3. Je kunt 'Hit' kiezen om een extra kaart te nemen of 'Stand' om te stoppen.\n
4. De dealer speelt na de speler en moet minstens 17 halen.\n
5. Ga je over de 21? Dan verlies je automatisch."""
        
        rules_label = tk.Label(self, text=rules_text, font=("Arial", 14), bg="darkgreen", fg="white", justify="left")
        rules_label.pack(pady=20, padx=20)

        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        back_button.pack(pady=10)
