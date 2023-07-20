import random

# Define the ranks and suits for the cards
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)

    def deal(self):
        if not self.is_empty():
            return self.cards.pop(0)
        return None

    def is_empty(self):
        return len(self.cards) == 0

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, card):
        self.hand.append(card)

    def play_card(self):
        if not self.is_hand_empty():
            return self.hand.pop(0)
        return None

    def is_hand_empty(self):
        return len(self.hand) == 0

def play_game():
    player1_name = input("Enter player 1's name: ")
    player2_name = input("Enter player 2's name: ")

    player1 = Player(player1_name)
    player2 = Player(player2_name)
    deck = Deck()

    for _ in range(len(deck.cards) // 2):
        player1.draw_card(deck.deal())
        player2.draw_card(deck.deal())

    while not player1.is_hand_empty() and not player2.is_hand_empty():
        input("Press Enter to play the next round...")
        card1 = player1.play_card()
        card2 = player2.play_card()

        print(f"{player1.name} plays: {card1}")
        print(f"{player2.name} plays: {card2}")

        if RANKS.index(card1.rank) > RANKS.index(card2.rank):
            print(f"{player1.name} wins this round!")
            player1.draw_card(card1)
            player1.draw_card(card2)
        elif RANKS.index(card1.rank) < RANKS.index(card2.rank):
            print(f"{player2.name} wins this round!")
            player2.draw_card(card1)
            player2.draw_card(card2)
        else:
            print("It's a tie! War!")
            player1.draw_card(card1)
            player2.draw_card(card2)

    if player1.is_hand_empty():
        print(f"\n{player2.name} wins the game!")
    else:
        print(f"\n{player1.name} wins the game!")

if __name__ == "__main__":
    play_game()
