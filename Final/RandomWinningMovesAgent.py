#Winning Move Training
import random
from Const import Const
from Move import Move
from Game import Game
from functools import lru_cache
import pickle

class RandomWinningMovesAgent:
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

        training_file = 'ReactiveTraining_RvR_1000_4x4.bin'
        try:
            input_file = open(training_file, 'rb')
            try:
                moveSets = pickle.load(input_file)
                moveScores = pickle.load(input_file)
            except (EOFError):
                print("SOMETHING WENT WRONG WHILE LOADING ", training_file)
        except (FileNotFoundError):
            print('No such file: ', training_file)
        if len(moveSets) == 0: print('Emtpy Training Sets')
        #else: print('I can work with this')

        for i in range(len(moveSets)):
            self.trainingSet.append((moveSets[i], moveScores[i]))

    def move(self,game,lastMove):
        playable = []
        lookForLargest = False
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
