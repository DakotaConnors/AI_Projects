from Const import Const
from Move import Move
from Game import Game
from GamePlay import GamePlay
from RandomAgent import RandomAgent
from WinningMoveTraining import WinningMoveTraining

class MinMaxVsRandomGamePlay(GamePlay):
    def createGame(self): return Game()
    def createAgentO(self): return RandomAgent()
    def createAgentX(self): return WinningMoveTraining(Const.MARK_X, 5) #Max depth of 5

def saveGameInfo(gameString):
    pass
    #save info here

if __name__ == '__main__':
    gameplay = MinMaxVsRandomGamePlay()
    gameString = gameplay.play()
    print('game over', gameString)
