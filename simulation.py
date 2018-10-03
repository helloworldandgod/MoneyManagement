

import roulettes
import mm


games= (roulettes.FairRoulette(mm.MartingaleMM()), roulettes.EuRoulette(mm.MartingaleMM()), roulettes.AmRoulette(mm.MartingaleMM())) 
#games = (roulettes.FairRoulette(mm.ConstantMM()), roulettes.EuRoulette(mm.ConstantMM()), roulettes.AmRoulette(mm.ConstantMM()))

trials = 20
spins = 1000000

def simulateGame(game, trials, spins):
    returns = []
    dropdowns = []
    for t in range(trials):
        trialValue,dropdown = roulettes.playRoulette(game,spins, 13, 1)
        returns.append(trialValue)
        dropdowns.append(dropdown)
    return returns, dropdowns

def calculateMeanAndStd(X):
    #mean = sum(X)/float(len(X))
    #tot=0.0
    #for x in X:
    #    tot+=(x - mean)**2
    #std = (tot/len(X))**0.5

    mean = sum(X)/float(len(X))
    tot = sum(list(map(lambda x: (x - mean)**2, X)))
    std = (tot/len(X))**0.5
    return mean, std


for G in games:
    returns, dropdowns = simulateGame(G, trials, spins)
    mean,std = calculateMeanAndStd(returns)
    dropmean, dropstd = calculateMeanAndStd(dropdowns)
    interval = 1.96*std*100
    #print(G.pockets)
    #print(interval) 
    #print("Game: ",G.__str__(),"; Expected return: ",mean*100,"; Interval confidence: ",mean*100-interval," - ",mean*100+interval)
    #print("Game: {:^20}; Expected return: {:10.2f}; Interval confidence: [{:4.2f} - {:4.2f}]".format(G.__str__(), mean*100, mean*100-interval,mean*100+interval))
    #print("Dropdown mean: {}, +/- {}\n".format(dropmean, dropstd))
    #print("Dropdowns {}".format(dropdowns))
    print("{} with {}".format(G.__str__(),G.nameMM()))
    print("==============================================")
    print("Expected return: {:.2f} with an interval confidence of [{:4.2f} - {:4.2f}]".format(mean*100, mean*100-interval,mean*100+interval))
    print("Dropdown mean: {:.2f}, +/- {:.2f}\n".format(dropmean,dropstd))
            
