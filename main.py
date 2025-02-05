import tkinter as tk
from tkinter import ttk
from package import BettingAppGUI, Player, set_dpi_awareness

# Zorgt ervoor dat de UI correct schaalt op high-DPI schermen (bijv. 4K-monitoren)
set_dpi_awareness()


class GameInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Titel en grootte van het hoofdvenster
        self.title("Blackjack Game")
        self.geometry("1560x910")
        self.resizable(False, False)  # Voorkomt dat het venster wordt geschaald

        self.frames = dict()  # Dictionary om frames (schermen) op te slaan

        # Stijlen instellen voor een consistente UI
        style = ttk.Style()
        style.theme_use('vista')  # Thema voor een nette uitstraling
        style.configure('Custom.TFrame', background='#007700', foreground='#FFFFFF')  # Achtergrond en tekstkleur
        style.configure('Custom.TButton', font=('Arial', 12), background='#007700')  # Stijl knoppen
        style.configure('Custom.TLabel', background='#007700', font="Arial 14 bold")  # Stijl labels

        # Hoofdcontainer voor het plaatsen van frames
        container = ttk.Frame(self, style="Custom.TFrame")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Speler-object aanmaken
        self.pl = Player()

        # Opslaan van de oorspronkelijke en huidige bankwaarde van de speler
        self.initial_bank_value = self.pl.bank
        self.bank_value = self.pl.bank
        self.bet_amount = 0  # Inzetbedrag van de speler

        # Flags om te bepalen of er een inzet is geplaatst en of de ronde is voltooid
        self.hasBetBeenPlaced = False
        self.roundComplete = False

        # Creëer en configureer het inzetvenster
        self.bettingFrame = BettingAppGUI(container, self)
        self.bettingFrame.configure(height=910)
        self.frames[BettingAppGUI] = self.bettingFrame  # Opslaan in frames dictionary
        self.bettingFrame.grid(row=0, column=0, sticky="nsew")  # Plaatsen in het grid


# Start de applicatie en vang eventuele fouten op
try:
    game_interface = GameInterface()
    game_interface.mainloop()
except:
    import traceback    
    traceback.print_exc()  # Geeft een foutmelding weer in de console
    input("Press Enter to end...")  # Wacht op input voordat het script sluit
