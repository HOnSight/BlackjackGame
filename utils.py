from PIL import Image, ImageTk
import random

# Kaartendek en waardes
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Maak en schud het deck (6 decks)
deck = [f"{rank} of {suit}" for rank in ranks for suit in suits] * 6
random.shuffle(deck)

# Laad kaartafbeeldingen
def load_card_images():
    card_images = {}
    for suit in suits:
        for rank in ranks:
            # Zet de rank om naar een 2-cijferig getal, zoals 02, 03, ...
            rank_index = ranks.index(rank) + 2  # Voeg 2 toe omdat de ranglijst start bij '2'
            rank_str = str(rank_index).zfill(2)
            
            # Maak de afbeelding naam op basis van de naam van de kaart
            card_name = f"card_{suit.lower()}_{rank_str}.png"
            card_path = f"cards/{card_name}"  # Verander hier naar 'cards/' zonder 'assets/'
            
            try:
                # Open en resize de afbeelding
                image = Image.open(card_path).resize((75, 100))
                card_images[f"{rank} of {suit}"] = ImageTk.PhotoImage(image)
            except FileNotFoundError:
                print(f"⚠️ Waarschuwing: {card_name} niet gevonden. Deze kaart wordt overgeslagen.")
    
    return card_images


# ✅ Opgelost: deal_card() accepteert nu een hand als argument
def deal_card(hand):
    if deck:
        card = deck.pop()
        hand.append(card)
        return card
    else:
        print("⚠️ Deck is leeg! Shuffle opnieuw nodig.")

# Bereken score
def calculate_score(hand):
    score = sum(values[card.split(' ')[0]] for card in hand)
    aces = sum(1 for card in hand if 'Ace' in card)
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score
