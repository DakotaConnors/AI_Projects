from Const import Const
from Move import Move
from Game import Game
from RandomAgent import RandomAgent

class GamePlay:
    def __init__(self):
        self._game = None
        self._agentO = None
        self._agentX = None

    def getGame(self):
        if self._game == None:
            self._game = self.createGame()
        return self._game

    def getAgentO(self):
        if self._agentO == None:
            self._agentO = self.createAgentO()
        return self._agentO

    def getAgentX(self):
        if self._agentX == None:
            self._agentX = self.createAgentX()
        return self._agentX

    def turn(self, lastMove, agent):
        game=self.getGame()
        state=game.getState()
        if state == Const.STATE_TURN_O: #Agent 0 is the random agent
            move = self.getAgentO().move(game, lastMove)
            #print(move)
            move.play(game)
            if (agent == 'Reactive'): lastMove = move
            return str(move), lastMove
        elif state == Const.STATE_TURN_X:
            move = self.getAgentX().move(game, lastMove)
            #print(move)
            move.play(game)
            if (agent == 'Offensive'): lastMove = move
            return str(move), lastMove
        else:
            raise ValueError("invalid game state (" + Const.stateStr(game.getState()) + ")")

    def play(self, agent):
        gameString = ''
        lastMove = ''
        game = self.getGame()
        while not game.over():
            addString, lastMove = self.turn(lastMove, agent)
            gameString += addString
        #print (Const.stateStr(game.getState()))
        if Const.stateStr(game.getState()) == 'x won': winner = 'x'
        elif Const.stateStr(game.getState()) == 'o won': winner = 'o'
        else: winner = 'd'
        return gameString, winner
