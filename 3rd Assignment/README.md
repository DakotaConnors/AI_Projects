CacheAgent.py

The cache is saved in the CacheAgent Class

in moveValue the agent checks if a value has already been cached to evaluate the move score
if not it finds the value and adds it to the cache

for game in game.SameGame():
            
  i = game.getIndex()
            
  if i in self._cache:
                
    print('Caching Value')
                
    return self._cache[i]

        

  ans = self.Value(game, self.maxDepth, depth)
        
  self._cache[i]=ans