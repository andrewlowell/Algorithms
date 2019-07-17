#!/usr/bin/python

import sys
  
def rock_paper_scissors(n):
  if n == 1:
    return [['rock'], ['paper'], ['scissors']]
  else:
    computed = rock_paper_scissors(n - 1)
    new_rps = []
    for play in computed:
      new_rps.append(play + ['rock'])
      new_rps.append(play + ['paper'])
      new_rps.append(play + ['scissors'])
    print(len(new_rps))
  return new_rps

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')