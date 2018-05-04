import random
from Const import Const
from Move import Move
from Game import Game
from functools import lru_cache

class MinMaxDepthAgent:
    def __init__(self, side, maxDepth):
        if side != Const.MARK_O and side != Const.MARK_X:
            raise ValueError("side must be MARK_X or MARK_O")
        self._side = side
        self._valueCache = {}
        self._cached = 0
        self.maxDepth = maxDepth


    def uncachedValue(self,game, maxDepth, currentDepth):
        currentDepth = currentDepth + 1
        #print(currentDepth)
        ans = None
        state = game.getState()
        if state == Const.STATE_WIN_O:
            if self._side == Const.MARK_O: ans = 1
            else: ans = -1
        elif state == Const.STATE_WIN_X:
            if self._side == Const.MARK_X: ans = 1
            else: ans = -1
        elif state == Const.STATE_DRAW:
            ans = 0

        if ans != None: return (ans,0)

        iside = 0
        if self._side == Const.MARK_O: iside = 1
        else: iside = -1

        iturn = 0
        if state == Const.STATE_TURN_O: iturn = 1
        else: iturn = -1

        myTurn = (iside == iturn)
        myOptions = 0

        if currentDepth == self.maxDepth:
            #pass
            return self.heuristicValue(game)
        for move in game.getMoves():
            move.play(game)
            (moveValue,moveOptions)=self.value(game, currentDepth)
            move.unplay(game)
            myOptions = myOptions + 1 + moveOptions
            if ans == None:
                ans = moveValue
            else:
                if myTurn:
                   ans = max(ans,moveValue)
                else:
                   ans = min(ans,moveValue)
        print ('This move is', ans)
        return (ans,myOptions)

    def heuristicValue(self,game):
        print('Hit the depth limit, not sure about move')
        return 0,0
        #if game.over(): return self.uncachedValue(game)[0]
        #xscore = 0
        #oscore = 0
        #for row in range(Const.ROWS):
        #    for col in range(Const.COLS):
        #        if game._board[row][col] == Const.MARK_NONE:
        #          for drow in range(-1,2):
        #              for dcol in range(-1,2):
        #                  nbrRow = row + drow
        #                  nbrCol = col + dcol
        #                  if (nbrRow >= 0 and nbrRow < Const.ROWS):
        #                      if (nbrCol >= 0 and nbrCol < Const.COLS):
        #                          if game._board[nbrRow][nbrCol] == Const.MARK_X:
        #                              xscore = xscore + 1
        #                          if game._board[nbrRow][nbrCol] == Const.MARK_O:
        #                              oscore = oscore + 1
        #if xscore == oscore: return 0
        #if self._side == Const.MARK_X:
        #    return float(xscore-oscore)/float(xscore+oscore)
        #else:
        #    return float(oscore-xscore)/float(xscore+oscore)

    def value(self,game,depth):
        #print('current depth: ' + str(depth))
        for equivGame in game.SameGame():
            index = equivGame.getIndex()
            if index in self._valueCache: return self._valueCache[index]
        ans = self.uncachedValue(game, self.maxDepth, depth) #Sending 0 for current depth
        #ans = self.heuristicValue(game)
        self._valueCache[index]=ans
        return ans

    def move(self,game):
        (maxValue,maxOptions)=self.value(game, 0)
        #print('value = ' + str(self.value(game)))
        playable = []
        maxPlayableOption = 0
        for move in game.getMoves():
            move.play(game)
            (moveValue,moveOptions)=self.value(game, 0)
            move.unplay(game)
            if moveValue == maxValue:
                playable.append((move,moveOptions))
                maxPlayableOption = max(maxPlayableOption,moveOptions)

        bestPlayable = []
        for (move,options) in playable:
            if options == maxPlayableOption:
                bestPlayable.append(move)

        spot=random.randint(0,len(bestPlayable)-1)
        return bestPlayable[spot]
