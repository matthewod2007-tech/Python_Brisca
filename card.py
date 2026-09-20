from abc import ABC,abstractmethod

class Card(ABC):
    def __init__(self,rank,points,power,suitName):
        self.rank = rank
        self.points = points
        self.power = power
        self.suitName = suitName

    def getRank(self):
        return self.rank

    def getPoints(self):
        return self.points

    def getPower(self):
        return self.power

    def getSuitName(self):
        return self.suitName

    def __str__(self):
        return f"{self.rank} of {self.suitName} ({self.points} points)"


class oro(Card):
    def __init__(self, rank, points, power, suitName):
        super().__init__(rank, points, power, suitName)

class espada(Card):
    def __init__(self, rank, points, power, suitName):
        super().__init__(rank, points, power, suitName)

class batuco(Card):
    def __init__(self, rank, points, power, suitName):
        super().__init__(rank, points, power, suitName)

class copa(Card):
    def __init__(self, rank, points, power, suitName):
        super().__init__(rank, points, power, suitName)