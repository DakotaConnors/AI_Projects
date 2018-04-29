import random
from Const import Const
from Move import Move
from Game import Game
from functools import lru_cache

class CacheAgent:
    def __init__(self, side, maxDepth):
        if side != Const.MARK_O and side != Const.MARK_X:
            raise ValueError("side must be MARK_X or MARK_O")
        self._side = side
        self._cache = {}
        self.maxDepth = maxDepth


    def Value(self,game, maxDepth, currentDepth):
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
            #print('Hit the depth limit, not sure about move')
            #Currently if it hits the depth limit the agent makes the move a '0'
            return 0,0
        for move in game.getMoves():
            move.play(game)
            (moveValue,moveOptions)=self.moveValue(game, currentDepth)
            move.unplay(game)
            myOptions = myOptions + 1 + moveOptions
            if ans == None:
                ans = moveValue
            else:
                if myTurn:
                   ans = max(ans,moveValue)
                else:
                   ans = min(ans,moveValue)
        #print ('This move is', ans)
        return (ans,myOptions)

    def moveValue(self,game,depth):
        for game in game.SameGame():
            i = game.getIndex()
            if i in self._cache:
                print('Caching Value')
                return self._cache[i]

        ans = self.Value(game, self.maxDepth, depth)
        self._cache[i]=ans
        return ans

    def move(self,game):
        (maxValue,maxOptions)=self.moveValue(game, 0)
        #print('value = ' + str(self.moveValue(game)))
        playable = []
        maxPlayableOption = 0
        for move in game.getMoves():
            move.play(game)
            (moveValue,moveOptions)=self.moveValue(game, 0)
            move.unplay(game)
            if moveValue == maxValue:
                playable.append((move,moveOptions))
                maxPlayableOption = max(maxPlayableOption,moveOptions)

        bestPlayable = []
        for (move,options) in playable:
            if options == maxPlayableOption:
                bestPlayable.append(move)

        #print(len(bestPlayable))
        spot=random.randint(0,len(bestPlayable)-1)
        return bestPlayable[spot]
