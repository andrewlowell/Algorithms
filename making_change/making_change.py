#!/usr/bin/python

import sys

cache = {
  5: 2,
  10: 4,
  15: 4,
  20: 5
}

def making_change(amount, denominations):

  global cache

  # *** If the amount of change is less than the smallest coin available, there are zero ways to make change
  if amount <= min(denominations):
    return 1

  total_ways_to_make_change = 1

  # *** Loop through the list of coins, starting with the highest denomination
  for index, coin in enumerate(reversed(denominations)):

    print(f"Index and coin are {index} and {coin}")

    # *** Only if the coin is less than the amount
    if coin < amount:

      print(f"Coin less than amount: {amount} - {coin} = {amount - coin}")

      # *** Add the number of ways you can make change with the remainder to the total

      if not (amount - coin) in cache:
        cache[amount - coin] = making_change(amount - coin, denominations[index:])
        print(f"Cached {amount - coin} = {cache[amount - coin]}")
      
      total_ways_to_make_change += cache[amount - coin]
      print(f"Adding {cache[amount - coin]} ways to make change")

  return total_ways_to_make_change

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")