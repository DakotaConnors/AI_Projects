import unittest
from Const import Const
from Game import Game

class TestState(unittest.TestCase):
    def testConstruct(self):
        unit = Game()
        self.assertEqual(unit.getState(),Const.STATE_TURN_O)

    def testXWin(self):
        unit = Game()
        unit.play("oa2 xa1 oa3 xb1 ob2 xc1")
        self.assertEqual(unit.getState(),Const.STATE_WIN_X)

    def testOWin(self):
        unit = Game()
        unit.play("oc1 xa2 oa1 xa3 ob1")
        self.assertEqual(unit.getState(),Const.STATE_WIN_O)

    def testDraw(self):
        unit = Game()
        unit.play("oa1 xa2 ob2 xc3 oc2 xa3 ob3 xb1 oc1")
        self.assertEqual(unit.getState(),Const.STATE_DRAW)
if __name__ == '__main__':
    unittest.main()
