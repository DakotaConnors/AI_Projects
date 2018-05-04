#Winning Move Training
import random
from Const import Const
from Move import Move
from Game import Game
from functools import lru_cache
import pickle

class BestWinningMovesAgent:
    def __init__(self, side, maxDepth):
        if side != Const.MARK_O and side != Const.MARK_X:
            raise ValueError("side must be MARK_X or MARK_O")
        self._side = side
        self._cache = {}
        self._cached = 0
        self.maxDepth = maxDepth
        self.trainingSet = []

        moveSets = []
        moveScores = []

        training_file = 'ReactiveTraining_RvWMA_100000_4x4.bin'
        try:
            input_file = open(training_file, 'rb')
            try:
                moveSets = pickle.load(input_file)
                moveScores = pickle.load(input_file)
            except (EOFError):
                print("SOMETHING WENT WRONG WHILE LOADING", training_file)
        except (FileNotFoundError):
            print('No such file:', training_file)
        if len(moveSets) == 0: print('Emtpy Training Sets')
        #else: print('I can work with this')

        for i in range(len(moveSets)):
            self.trainingSet.append((moveSets[i], moveScores[i]))

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

    def heuristicValue(self,game):
        #print('Hit the depth limit, not sure about move')
        #Currently if it hits the depth limit the agent makes the move a '0'
        return 0,0

    def moveValue(self,game,depth):

        ans = self.uncachedValue(game, self.maxDepth, depth)
        #self._cache[i]=ans
        return ans

    def move(self,game,lastMove):
        playable = []
        lookForLargest = True
        backUpPlan = False
        largestScore = 0
        bestMove = None

        for move in game.getMoves():
            for set in self.trainingSet:
                if ((str(lastMove) in set[0]) and (str(move) in set[0])):
                    if set[1] > 0:
                        if lookForLargest:
                            if largestScore < set[1]:
                                largestScore = set[1]
                                bestMove = move
                        else: playable.append(move)

        if bestMove != None:
            playable.append(move)
            #playable.append(move)



        if len(playable) == 0:
            if backUpPlan:
                largestScore = -9999999
                for move in game.getMoves():
                    for set in self.trainingSet:
                        if ((str(lastMove) in set[0]) and (str(move) in set[0])):
                            if largestScore < set[1]:
                                largestScore = set[1]
                                bestMove = move
                if bestMove != None:
                    playable.append(move)
                else:
                    for move in game.getMoves():
                        playable.append(move)
            else:
                for move in game.getMoves():
                    playable.append(move)
        spot=random.randint(0,len(playable)-1)
        return playable[spot]
