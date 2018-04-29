from Const import Const
from Move import Move
from Game import Game
from GamePlay import GamePlay
from RandomAgent import RandomAgent
from CacheAgent import CacheAgent

class MinMaxVsRandomGamePlay(GamePlay):
    def createGame(self): return Game()
    def createAgentO(self): return RandomAgent()
    def createAgentX(self): return CacheAgent(Const.MARK_X, 5) #Max depth of 5

if __name__ == '__main__':
    gameplay = MinMaxVsRandomGamePlay()
    gameplay.play()
