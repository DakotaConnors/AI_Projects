import unittest
from Const import Const
from Game import Game
from MinMaxAgent import MinMaxAgent
class TestMinMaxAgent(unittest.TestCase):
    def testFavorOXWins(self):
        game = Game()
        agent = MinMaxAgent(Const.MARK_O)
        game.play("oa2 xa1 oa3 xb1 ob2 xc1")
        self.assertEqual(agent.heuristicValue(game),-1)

    def testFavorOXNearlyWins(self):
        game = Game()
        agent = MinMaxAgent(Const.MARK_O)
        game.play("oa2 xa1 oa3 xb1 ob2")
        self.assertEqual(agent.heuristicValue(game),0.5)        

if __name__ == '__main__':
    unittest.main()
