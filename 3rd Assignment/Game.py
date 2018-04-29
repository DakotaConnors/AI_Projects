from Const import Const
from Move import Move

class Game:
    def over(self):
        return \
            self._state == Const.STATE_WIN_O or \
            self._state == Const.STATE_WIN_X or \
            self._state == Const.STATE_DRAW

    def moveOk(self,row,col,mark):
        Const.rowOk(row)
        Const.colOk(col)
        Const.markOk(mark)
        if (self._state == Const.STATE_TURN_O) and (mark == Const.MARK_O) and \
           self._board[row][col] == Const.MARK_NONE:
           return
        if (self._state == Const.STATE_TURN_X) and (mark == Const.MARK_X) and \
           self._board[row][col] == Const.MARK_NONE:
           return
        raise ValueError("move (" + str(Move(mark,row,col)) + ") invalid in current state")

    def getMoves(self):
        mark = None
        if self._state == Const.STATE_TURN_O:
            mark = Const.MARK_O
        elif self._state == Const.STATE_TURN_X:
            mark = Const.MARK_X

        if mark == None:
            return []

        moves = []
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                if self._board[row][col] == Const.MARK_NONE:
                    moves.append(Move(row,col,mark))

        return moves

    def _repeats(self,row,col,rowDir,colDir):
        mark = self._board[row][col]
        count = 0
        while (row >= 0 and row < Const.ROWS and col >= 0) and \
              col < Const.COLS and self._board[row][col]==mark:
            row=row+rowDir
            col=col+colDir
            count = count + 1
        return count

    def _length(self,row,col,rowDir,colDir):
        return self._repeats(row,col,rowDir,colDir)+self._repeats(row,col,-rowDir,-colDir)-1

    def _winRow(self,row,col):
        return self._length(row,col,1,0) >= Const.WIN_LENGTH
    def _winCol(self,row,col):
        return self._length(row,col,0,1) >= Const.WIN_LENGTH
    def _winMainDiag(self,row,col):
        return self._length(row,col,1,1) >= Const.WIN_LENGTH
    def _winOffDiag(self,row,col):
        return self._length(row,col,1,-1) >= Const.WIN_LENGTH

    def _win(self,row,col):
        return self._winRow(row,col) or self._winCol(row,col) or \
               self._winMainDiag(row,col) or self._winOffDiag(row,col)

    def _draw(self):
        return self._unplayed == 0

    def move(self,row,col,mark):
        self.moveOk(row,col,mark)
        self._board[row][col]=mark
        self._unplayed = self._unplayed - 1
        if self._win(row,col):
            if mark == Const.MARK_O:
                self._state = Const.STATE_WIN_O
            if mark == Const.MARK_X:
                self._state = Const.STATE_WIN_X
        elif self._draw():
            self._state = Const.STATE_DRAW
        else:
            if mark == Const.MARK_O:
                self._state = Const.STATE_TURN_X
            if mark == Const.MARK_X:
                self._state = Const.STATE_TURN_O

    def unmove(self,row,col):
        Const.rowOk(row)
        Const.colOk(col)
        if self._board[row][col] == Const.MARK_X:
            self._unplayed = self._unplayed + 1
            self._board[row][col] = Const.MARK_NONE
            self._state = Const.STATE_TURN_X
        elif self._board[row][col] == Const.MARK_O:
            self._unplayed = self._unplayed + 1
            self._board[row][col] = Const.MARK_NONE
            self._state = Const.STATE_TURN_O
        else:
            raise ValueError("unmove (" + str(row) + "," + str(col) + ") invalid in current state")

    def reset(self):
        self._board = [[Const.MARK_NONE for col in range(Const.COLS)] for row in range(Const.ROWS)]

        self._state = Const.STATE_TURN_O
        self._unplayed = Const.ROWS*Const.COLS

    def getBoard(self):
        return [[self._board[row][col]  for col in range(Const.COLS)] for row in range(Const.ROWS)]

    def getState(self):
        return self._state

    def __init__(self):
        self.reset()

    def play(self,moves):
        for move in moves.split():
            Move.parse(move).play(self)

    def __str__(self):
        ans = "\n"
        for row in range(Const.ROWS):
            s="";
            for col in range(Const.COLS):
                s=s+Const.markStr(self._board[row][col])
            ans = ans + s + "\n"
        return ans

    def copyTo(self,target):
        target._board = [[self._board[row][col] for col in range(Const.COLS)] for row in range(Const.ROWS)]
        target._state = self._state
        target._unplayed = self._unplayed

    def clone(self):
        ans = Game()
        self.copyTo(ans)
        return ans

    def __hash__(self):
        tuple = (self._board[k % Const.ROWS][k // Const.ROWS] for k in range(Const.ROWS*Const.COLS))
        return hash(tuple)

    def __eq__(self, other):
        return other != None and (self._board == other._board)

    def __ne__(self, other):
        return not self.__eq__(other)

    def getIndex(self):
        i = 0
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                board=self._board[row][col]
                x = 0
                if board == Const.MARK_X:
                    x = 1
                elif board == Const.MARK_O:
                    x = 2
                i = 3*i + x
        #print (i)
        return i

    def flipRows(self):
        ans=self.clone()
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                ans._board[Const.ROWS-row-1][col]=self._board[row][col]
        return ans

    def flipCols(self):
        ans = self.clone()
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                ans._board[row][Const.COLS-col-1]=self._board[row][col]
        return ans

    def flipRowsAndCols(self):
        ans = self.clone()
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                ans._board[Const.ROWS-row-1][Const.COLS-col-1]=self._board[row][col]
        return ans

    def transpose(self):
        if Const.ROWS != Const.COLS: return None
        ans = self.clone()
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                ans._board[col][row]=self._board[row][col]
        return ans

    def offDiagonalTranspose(self):
        if Const.ROWS != Const.COLS: return None
        return self.flipRows().transpose()

    def SameGame(self):
        _game = [self.clone(), self.flipRows(), self.flipCols(), self.flipRowsAndCols()]
        #print (game)
        return _game
