import random
from Const import Const
from Move import Move
from State import State

class SmarterAgent:
    def __init__(self):
        pass

    def move(self,state):
        mark = None
        if state.getState() == Const.STATE_TURN_O:
            mark = Const.MARK_O
        if state.getState() == Const.STATE_TURN_X:
            mark = Const.MARK_X
        if mark == None:
            raise ValueError("state must be playable")
        board = state.getBoard()
        playable = []
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                if board[row][col] == Const.MARK_NONE:
                    playable.append([row,col])
        #Instead of just picking a random spot. First check if there is a winnable Move
        tempMove = Move(0,0,mark)
        for i in range(len(playable)):
            tempMove.play(playable[i][0], playable[i][0])
            #if the spot makes X win then it returns the move
            if self._state.getState() == Const.STATE_WIN_X:
                tempMove.undo(state)
                return tempMove
            #otherwise undo and try the next on
            playable[i].undo(state)
        spot=random.randint(0,len(playable)-1)
        return Move(playable[spot][0],playable[spot][1],mark)
