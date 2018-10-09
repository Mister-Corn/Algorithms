#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  steps = [1, 2, 3]
  cache = [0 for i in range(n + 1)] if not cache else cache
  
  def inner_recurse(n, cache):
    result = 0

    if n < 0:
      return 0
    elif n == 0:
      return 1
    
    for step in steps:
      result += cache[n - step] if cache[n - step] != 0 else inner_recurse(n - step, cache)
    
    cache[n] = result
    return cache[n] if cache[n] != 0 else result
  
  return inner_recurse(n, cache)
  
 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')