import tkinter as tk

# Functie voor de spelregels pagina
def create_rules_page(root):
    rules_frame = tk.Frame(root, bg="darkgreen")

    # Titel van de pagina
    rules_title = tk.Label(rules_frame, text="Spelregels van Blackjack", font=("Arial", 24), bg="darkgreen", fg="white")
    rules_title.pack(pady=20)

    # Spelregels tekst
    rules_text = """Blackjack is een populair kaartspel waarbij je probeert een hand van kaarten te maken die zo dicht mogelijk bij 21 komt, zonder deze waarde te overschrijden.
    
1. Elke speler krijgt twee kaarten, en de dealer krijgt ook twee kaarten, maar één van de kaarten is zichtbaar.
2. Kaarten van 2 tot 10 zijn hun waarde, terwijl de boer, dame en koning als 10 tellen, en een aas als 1 of 11 kan worden gebruikt.
3. Spelers kunnen kiezen om extra kaarten te trekken ('hit') of te blijven staan ('stand').
4. Het doel is om de dealer te verslaan zonder meer dan 21 punten te halen."""

    rules_label = tk.Label(rules_frame, text=rules_text, font=("Arial", 14), bg="darkgreen", fg="white", justify="left")
    rules_label.pack(pady=20)

    # Terug naar Home knop
    back_button = tk.Button(rules_frame, text="Terug naar Home", command=lambda: show_home_page(root, rules_frame), bg="white", font=("Arial", 16))
    back_button.pack(pady=20)

    rules_frame.pack(fill="both", expand=True)

# Functie om terug te keren naar de home pagina
def show_home_page(root, rules_frame):
    rules_frame.pack_forget()  # Verberg de regels-pagina
    from home_page import create_home_page  # Importeer de functie uit home_page.py
    create_home_page(root)  # Laad de Home-pagina opnieuw
