import tkinter as tk
from home_page import create_home_page  # Zorg ervoor dat home_page.py correct wordt geïmporteerd
from game_page import create_game_page  # Zorg ervoor dat game_page.py correct wordt geïmporteerd

def main():
    # Maak het hoofdvenster van de toepassing
    root = tk.Tk()
    root.title("Blackjack Game")  # Geef het venster een titel
    root.geometry("800x600")  # Pas de grootte van het venster aan
    root.configure(bg="darkgreen")  # Zet de achtergrondkleur van het venster
    
    # Start de homepagina
    create_home_page(root)
    
    # Start de GUI
    root.mainloop()

if __name__ == "__main__":
    main()
