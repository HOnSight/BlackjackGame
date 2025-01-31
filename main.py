import tkinter as tk
from home_page import create_home_page
from rules import create_rules_page
from package import BettingAppGUI, Player, set_dpi_awareness

set_dpi_awareness()

class GameInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blackjack Game")
        self.geometry("1560x910")
        self.resizable(False, False)

        self.frames = {}

        self.show_home_page()

    def show_home_page(self):
        """Toont de homepagina."""
        self.clear_frames()
        self.home_frame = create_home_page(self, self.show_game_page, self.show_rules_page)

    def show_rules_page(self, prev_frame):
        """Toont de regels en verbergt de vorige pagina."""
        prev_frame.pack_forget()
        self.rules_frame = create_rules_page(self, self.show_home_page)

    def show_game_page(self, prev_frame):
        """Start het spel en verbergt de homepagina."""
        prev_frame.pack_forget()
        self.start_game()

    def start_game(self):
        """Start de Blackjack-game."""
        container = tk.Frame(self, bg="darkgreen")
        container.pack(fill="both", expand=True)

        self.pl = Player()
        self.bettingFrame = BettingAppGUI(container, self)
        self.frames[BettingAppGUI] = self.bettingFrame
        self.bettingFrame.grid(row=0, column=0, sticky="nsew")

    def clear_frames(self):
        """Verwijdert alle actieve frames."""
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    game_interface = GameInterface()
    game_interface.mainloop()
