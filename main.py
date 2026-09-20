#file of the player interface
import game as g
import deck as d

GameDeck = d.deck()
GameDeck.shuffleDeck()

cards = GameDeck.cards

playercards = []

playercards = g.giveCards(cards)

for c in playercards:
    print(c)

