#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  steps = [1, 2, 3]
  num_ways = 0
  
  def inner_recurse(n):
    nonlocal num_ways

    if n < 0:
      return 0
    elif n == 0:
      num_ways += 1
      return
    
    for step in steps:
      inner_recurse(n - step)
  
  inner_recurse(n)
  return num_ways
 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')