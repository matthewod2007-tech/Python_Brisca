from card import oro,espada,batuco,copa
# files with all the methods of the game

cardLimit = 3

def giveCards(shuffled):
    cards = []
    for c in range(cardLimit):
        cards.append(shuffled.pop(0))
    return cards

def refill(shuffle,hand):
    if(hand <=0 ):
        return
    while len(hand) > 3:
        if not shuffle:
            break
        hand.append(shuffle.pop(0))

def winnerOfHand(hand , aiHand , card1 , card2 , trump):
    UserCard = hand[card1-1]
    AiCard = aiHand[card2-1]

    playerTrump = UserCard.getSuitName()
    AiTrump = AiCard.getSuitName()

    trumpW = trump.getSuitName()

