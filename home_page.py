import tkinter as tk
from tkinter import ttk
from package import BettingAppGUI, Player, set_dpi_awareness
from start_page import StartPage
from rules import RulesPage  # Voeg een rules-pagina toe als extra scherm

set_dpi_awareness()

class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blackjack Game")
        self.geometry("1560x910")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use('vista')
        style.configure('Custom.TFrame', background='#007700', foreground='#FFFFFF')
        style.configure('Custom.TButton', font=('Arial', 12), background='#007700')
        style.configure('Custom.TLabel', background='#007700', font="Arial 14 bold")

        self.frames = {}

        container = ttk.Frame(self, style="Custom.TFrame")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Voeg pagina's toe
        for F in (StartPage, RulesPage, GameInterface):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Toont de gewenste pagina"""
        frame = self.frames[page_name]
        frame.tkraise()


class GameInterface(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="darkgreen")

        self.pl = Player()
        self.initial_bank_value = self.pl.bank
        self.bank_value = self.pl.bank
        self.bet_amount = 0

        self.hasBetBeenPlaced = False
        self.roundComplete = False

        self.bettingFrame = BettingAppGUI(self, controller)
        self.bettingFrame.configure(height=910)
        self.bettingFrame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
