import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Functies voor kaartdealen en scoreberekeningen
def load_card_images():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    card_images = {}
    
    for suit in suits:
        for value in values:
            image_path = f"assets/card_{suit}_{value}.png"
            try:
                image = Image.open(image_path)
                card_images[f"{value}_of_{suit}"] = ImageTk.PhotoImage(image)
            except FileNotFoundError:
                print(f"Image {image_path} not found.")
    
    return card_images

def deal_card(hand, card_images):
    card_values = list(card_images.keys())
    card = random.choice(card_values)
    hand.append(card)
    return card

def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        value = card.split('_')[0]  # Haal de waarde van de kaart uit
        if value in ['J', 'Q', 'K']:
            score += 10
        elif value == 'A':
            aces += 1
            score += 11
        else:
            score += int(value)
    
    # Verwerk de Azen (als 11 of 1)
    while score > 21 and aces:
        score -= 10
        aces -= 1
    
    return score

# Hoofdgame pagina
def hit(game_frame, player_hand, card_images, player_frame):
    card = deal_card(player_hand, card_images)
    score = calculate_score(player_hand)
    
    # Laad de afbeelding van de kaart
    card_image = card_images[card]
    
    # Voeg de kaart toe aan het spelerframe
    card_label = tk.Label(player_frame, image=card_image, bg="darkgreen")
    card_label.image = card_image  # Bewaar de referentie
    card_label.pack(side="left", padx=10)

    # Toon de score van de speler
    score_label.config(text=f"Player's Score: {score}")
    
    if score > 21:
        messagebox.showinfo("Game Over", "You busted! Dealer wins.")
        return False  # Eindig het spel
    return True

def stand(game_frame, dealer_hand, player_hand, card_images, dealer_frame, player_frame):
    # Verberg de spelersecho en laat de dealer spelen
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    
    # Dealer trekt kaarten totdat hij minimaal 17 heeft
    while dealer_score < 17:
        card = deal_card(dealer_hand, card_images)
        card_image = card_images[card]
        card_label = tk.Label(dealer_frame, image=card_image, bg="darkgreen")
        card_label.image = card_image
        card_label.pack(side="left", padx=10)
        dealer_score = calculate_score(dealer_hand)
    
    # Toon scores en bepaal winnaar
    if dealer_score > 21 or player_score > dealer_score:
        messagebox.showinfo("Game Over", "You win!")
    elif dealer_score > player_score:
        messagebox.showinfo("Game Over", "Dealer wins!")
    else:
        messagebox.showinfo("Game Over", "It's a tie!")
    
    game_frame.quit()  # Stop het spel

def create_game_page(root):
    game_frame = tk.Frame(root, bg="darkgreen")
    
    # Speler en dealer hand
    player_hand = []
    dealer_hand = []

    # Kaartafbeeldingen laden
    card_images = load_card_images()

    # Frames voor kaarten en knoppen
    dealer_frame = tk.Frame(game_frame, bg="darkgreen")
    dealer_frame.pack(pady=10)

    player_frame = tk.Frame(game_frame, bg="darkgreen")
    player_frame.pack(pady=10)

    # Scorelabels
    global score_label
    score_label = tk.Label(game_frame, text="Player's Score: 0", font=("Arial", 16), bg="darkgreen", fg="white")
    score_label.pack(pady=20)

    # Dealing initial cards
    deal_card(player_hand, card_images)
    deal_card(dealer_hand, card_images)
    deal_card(player_hand, card_images)
    deal_card(dealer_hand, card_images)

    # Display initial cards for player and dealer
    for card in player_hand:
        card_image = card_images[card]
        card_label = tk.Label(player_frame, image=card_image, bg="darkgreen")
        card_label.image = card_image
        card_label.pack(side="left", padx=10)

    for card in dealer_hand:
        card_image = card_images[card]
        card_label = tk.Label(dealer_frame, image=card_image, bg="darkgreen")
        card_label.image = card_image
        card_label.pack(side="left", padx=10)

    # Knoppen
    button_frame = tk.Frame(game_frame, bg="darkgreen")
    button_frame.pack(pady=20)

    hit_button = tk.Button(button_frame, text="Hit", command=lambda: hit(game_frame, player_hand, card_images, player_frame), bg="white")
    hit_button.grid(row=0, column=0, padx=5)

    stand_button = tk.Button(button_frame, text="Stand", command=lambda: stand(game_frame, dealer_hand, player_hand, card_images, dealer_frame, player_frame), bg="white")
    stand_button.grid(row=0, column=1, padx=5)

    game_frame.pack(fill="both", expand=True)
