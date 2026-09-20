
import random as rd
from card import oro,espada,batuco,copa

class deck:
    def __init__(self):
        self.cards=[]
        self.build_deck()

    def build_deck(self):
        RANK = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        POINTS = [11, 0, 10, 0, 0, 0, 0, 2, 3, 4]
        
        POWER = [10, 1, 9, 2, 3, 4, 5, 6, 7, 8]

        for rank,points,power in zip(RANK,POINTS,POWER):
            self.cards.append(oro(rank,points=points,power=power,suitName="Oro"))
            self.cards.append(espada(rank,points=points,power=power,suitName="Espada"))
            self.cards.append(batuco(rank,points=points,power=power,suitName="Batuco"))
            self.cards.append(copa(rank,points=points,power=power,suitName="Copa"))

    def shuffleDeck(self):
        rd.shuffle(self.cards)
        