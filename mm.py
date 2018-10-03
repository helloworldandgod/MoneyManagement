

class ConstantMM():
    def __init__(self):
        self.results = []
        self.bet = 1

    def next(self):
        return 1

    def updateLastBet(self, result):
        self.results.append(result)

    def __str__(self):
        return 'Constant Money Management'


class MartingaleMM(ConstantMM):
    def next(self):
        #if last was lost then *2, else 1
        if len(self.results)>0 and self.results[-1]==0:
            self.bet *= 2
        else:
            self.bet = 1
        
        #print("Next bet: ",self.bet)
        return self.bet

    def __str__(self):
        return 'Martingale Money Management'
