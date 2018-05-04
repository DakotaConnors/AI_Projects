from Const import Const
from Move import Move
from Game import Game
from GamePlay import GamePlay
from RandomAgent import RandomAgent
from RandomWinningMovesAgent import RandomWinningMovesAgent
from BestWinningMovesAgent import BestWinningMovesAgent
from BackUpPlanAgent import BackUpPlanAgent
from OffensiveAgent import OffensiveAgent
import pickle
from datetime import datetime

save_file = 'RvWMA_100000.bin'

def loadGameStrings():
    gameStrings = []
    try:
        input_file = open(save_file, 'rb')
        try:
            gameStrings = pickle.load(input_file)
        except (EOFError):
            print("SOMETHING WENT WRONG WHILE LOADING")
    except (FileNotFoundError):
        pass
    #for g in gameStrings:
    #    print(g)
    return gameStrings

def saveGameInfo(gameStrings): #Creating a Training Set
    gameStrings.append(gameString + winner)
    output_file = open(save_file, "wb")
    pickle.dump(gameStrings, output_file)
    output_file.close()

class PlayManyGames(GamePlay):
    def createGame(self): return Game()
    def createAgentO(self): return OffensiveAgent(Const.MARK_X, 5)
    def createAgentX(self): return RandomAgent()
    #def createAgentX(self): return OffensiveAgent(Const.MARK_X, 5)
    #def createAgentX(self): return BackUpPlanAgent(Const.MARK_X, 5)
    #def createAgentX(self): return RandomWinningMovesAgent(Const.MARK_X, 5)
    #def createAgentX(self): return BestWinningMovesAgent(Const.MARK_X, 5)

if __name__ == '__main__':
    xwins = 0
    owins = 0
    games = 1000
    gameStrings = loadGameStrings()
    agent = 'Reactive'

    for i in range(games):
        gameplay = PlayManyGames()
        gameString, winner = gameplay.play(agent)
        if winner == 'x': xwins += 1
        elif winner == 'o': owins += 1
        if len(gameStrings) < 1000: gameStrings.append(gameString + winner)
        if i % 100 == 0: print(i, 'Games Played', datetime.now())
    #print(games, 'played')
    print('x wins ' + str(xwins) + '/' + str(games))
    print('o wins ' + str(owins) + '/' + str(games))
    print (str(games-owins-xwins),'draws')
    #saveGameInfo(gameStrings)
    #print(len(gameStrings))
