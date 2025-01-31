import tkinter as tk
from tkinter import messagebox
from utils import load_card_images, deal_card, calculate_score

def hit(game_frame):
    """Handles the 'Hit' action by adding a card to the player's hand."""
    player_hand = game_frame.player_hand
    card = deal_card(player_hand)  # Deel een kaart aan de speler
    score = calculate_score(player_hand)
    
    # Zoek de afbeelding van de kaart op basis van de naam
    card_image = game_frame.card_images.get(card)
    
    if card_image:
        # Voeg de afbeelding van de kaart toe aan de speler
        player_card_label = tk.Label(game_frame.player_frame, image=card_image, bg="green")
        player_card_label.image = card_image  # Bewaar referentie naar het beeld
        player_card_label.pack(side="left", padx=10)

    # Update de score van de speler
    game_frame.score_label.config(text=f"Score: {score}")

    if score > 21:
        messagebox.showinfo("Game Over", "You busted! Dealer wins.")

def stand(game_frame):
    """Handles the 'Stand' action by ending the player's turn."""
    dealer_hand = game_frame.dealer_hand
    score = calculate_score(dealer_hand)
    
    # Dealer neemt kaarten totdat de score minstens 17 is
    while score < 17:
        card = deal_card(dealer_hand)
        card_image = game_frame.card_images.get(card)
        if card_image:
            dealer_card_label = tk.Label(game_frame.dealer_frame, image=card_image, bg="green")
            dealer_card_label.image = card_image
            dealer_card_label.pack(side="left", padx=10)
        score = calculate_score(dealer_hand)
    
    dealer_score_label = tk.Label(game_frame.dealer_frame, text=f"Dealer Score: {score}", bg="green", fg="white")
    dealer_score_label.pack(pady=10)
    
    # Controleer de winnaar
    player_score = calculate_score(game_frame.player_hand)
    if player_score > 21:
        messagebox.showinfo("Game Over", "You busted! Dealer wins.")
    elif score > 21:
        messagebox.showinfo("Game Over", "Dealer busted! You win!")
    elif player_score > score:
        messagebox.showinfo("You Win!", "Your score is higher than the dealer's!")
    elif player_score < score:
        messagebox.showinfo("You Lose", "The dealer's score is higher!")
    else:
        messagebox.showinfo("Tie", "It's a tie!")

def create_game_page(root):
    game_frame = tk.Frame(root, bg="green")
    game_frame.player_hand = []  # Hand van de speler
    game_frame.dealer_hand = []  # Hand van de dealer

    # Laad de kaarten eenmaal
    game_frame.card_images = load_card_images()  # Laad alle afbeeldingen van de kaarten

    # Frames voor kaarten en buttons
    dealer_frame = tk.Frame(game_frame, bg="green")
    dealer_frame.pack(pady=10)

    game_frame.player_frame = tk.Frame(game_frame, bg="green")  # Dit frame bevat de kaarten van de speler
    game_frame.player_frame.pack(pady=10)

    # Toon de score van de speler
    game_frame.score_label = tk.Label(game_frame.player_frame, text="Score: 0", bg="green", fg="white")
    game_frame.score_label.pack(pady=10)

    # Buttons
    button_frame = tk.Frame(game_frame, bg="green")
    button_frame.pack(pady=20)

    hit_button = tk.Button(button_frame, text="Hit", command=lambda: hit(game_frame), bg="white")
    hit_button.grid(row=0, column=1, padx=5)

    stand_button = tk.Button(button_frame, text="Stand", command=lambda: stand(game_frame), bg="white")
    stand_button.grid(row=0, column=2, padx=5)

    leave_button = tk.Button(button_frame, text="Leave Table", command=lambda: show_home_page(root, game_frame), bg="white")
    leave_button.grid(row=0, column=3, padx=5)

    # Deel meteen 2 kaarten voor de speler en 1 voor de dealer
    for _ in range(2):
        card = deal_card(game_frame.player_hand)
        card_image = game_frame.card_images.get(card)
        if card_image:
            player_card_label = tk.Label(game_frame.player_frame, image=card_image, bg="green")
            player_card_label.image = card_image
            player_card_label.pack(side="left", padx=10)

    # Deel de dealer's eerste kaart
    dealer_card = deal_card(game_frame.dealer_hand)
    dealer_card_image = game_frame.card_images.get(dealer_card)
    if dealer_card_image:
        dealer_card_label = tk.Label(dealer_frame, image=dealer_card_image, bg="green")
        dealer_card_label.image = dealer_card_image
        dealer_card_label.pack(side="left", padx=10)

    # Deel de tweede kaart voor de dealer, maar laat deze verborgen
    dealer_card_back = Image.open("assets/card_back.png").resize((75, 100))  # Zorg voor een omgekeerde kaart
    dealer_card_back_image = ImageTk.PhotoImage(dealer_card_back)
    dealer_card_back_label = tk.Label(dealer_frame, image=dealer_card_back_image, bg="green")
    dealer_card_back_label.image = dealer_card_back_image
    dealer_card_back_label.pack(side="left", padx=10)

    game_frame.pack(fill="both", expand=True)
