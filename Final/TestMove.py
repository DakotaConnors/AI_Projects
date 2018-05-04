import unittest
from Move import Move
from State import State

class TestMove(unittest.TestCase):
    def testConstruct(self):
        row=1
        col=2
        mark=None
        unit = Move(row,col,mark)
        self.assertEqual(unit.getRow(),row)
        self.assertEqual(unit.getCol(),col)
        self.assertEqual(unit.getMark(),mark)

    def testConstructString1(self):
        str="b3"
        row=1
        col=2
        mark=None
        unit = Move.parse(str)
        self.assertEqual(unit.getRow(),row)
        self.assertEqual(unit.getCol(),col)
        self.assertEqual(unit.getMark(),mark)

    def testConstructString2(self):
        str="xa3"
        row=0
        col=2
        mark=State.BOARD_X
        unit = Move.parse(str)
        self.assertEqual(unit.getRow(),row)
        self.assertEqual(unit.getCol(),col)
        self.assertEqual(unit.getMark(),mark)

    def testConstructString3(self):
        str="oc1"
        row=2
        col=0
        mark=State.BOARD_O
        unit = Move.parse(str)
        self.assertEqual(unit.getRow(),row)
        self.assertEqual(unit.getCol(),col)
        self.assertEqual(unit.getMark(),mark)

if __name__ == '__main__':
    unittest.main()
        
