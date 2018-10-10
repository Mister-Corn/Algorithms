#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  moves = ['rock', 'paper', 'scissors']
  plays = []

  def inner_recurse(n, play):
    if n == 0:
      plays.append(play)
      return
    
    for move in moves:
      inner_recurse(n -1, play + [move])
  
  inner_recurse(n, [])
  return plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')