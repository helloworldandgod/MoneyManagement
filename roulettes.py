import random

class FairRoulette():
    def __init__(self,mm):
        self.pockets = 36
        self.odds = 35
        self.ball = None
        self.mm = mm

    def spin(self):
        self.ball = random.randint(0,self.pockets-1)
    
    def betPocket(self, pocket_bet, amount):
        if pocket_bet==self.ball:
            self.mm.updateLastBet(1)
            return amount*self.mm.next()*self.odds
        else:
            self.mm.updateLastBet(0)
            return -amount

    def betColour(self, colour, amount):
            size = self.mm.next()*amount
            if self.ball < 18 and colour==0:
                self.mm.updateLastBet(1)
            else:
                self.mm.updateLastBet(0)
                size *=-1
            return size

    def nameMM(self):
        return self.mm.__str__()

    def __str__(self):
        return 'Fair Roulette'

class EuRoulette(FairRoulette):
    def __init__(self,mm):
        FairRoulette.__init__(self,mm)
        self.pockets += 1

    def __str__(self):
        return 'European Roulette'

class AmRoulette(EuRoulette):
    def __init__(self,mm):
        EuRoulette.__init__(self,mm)
        self.pockets += 1

    def __str__(self):
        return 'American Roulette'

#Modificar amount por un objeto con el money management 
def playRoulette(game, spins, pocket_bet, amount):
    bank = 0
    dropdown = 0
    for i in range(spins):
        game.spin()
        #bank += game.betPocket(pocket_bet, amount)
        bank += game.betColour(0, amount)
        if bank < dropdown:
            dropdown = bank
    
    return bank/(spins*1.0),100*dropdown/(spins*1.0)

#random.seed(0)
#game = AmRoulette()

#tot = playRoulette(game, 1000000, 13, 1)

#print(game.pockets)
#print(game.__str__(),': ',tot*100,'%')
#print("hello world!",tot,"%")



