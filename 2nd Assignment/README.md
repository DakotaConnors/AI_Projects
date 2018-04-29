DepthLimitAgent.py is the MinMax agent with a depth Limit


class DepthLimitAgent:

  def __init__(self, side, maxDepth):
    if side != Const.MARK_O and side != Const.MARK_X:

      raise ValueError("side must be MARK_X or MARK_O")
        
    self._side = side
        
    self.maxDepth = maxDepth

Max depth allowed is stored in the agent Class



The current depth of the search is passed as a parameter:

def moveValue(self,game,depth):

def Value(self,game, maxDepth, currentDepth):
 
  currentDepth = currentDepth + 1



Finally when the max depth is reached it returns a 0 to signal it's unsure how good of a move it is

if currentDepth == self.maxDepth:
  print('Hit the depth limit, not sure about move')
  #Currently if it hits the depth limit the agent makes the move a '0'
  return 0,0