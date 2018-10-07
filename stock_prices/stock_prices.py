#!/usr/bin/python

import argparse
import math

"""
Possibly use Kadane's algorithm?
Seems to be good ol' subarrays messing with my head again
"""

debug = False

# def find_max_profit_brute(prices):
#   max_profit = -math.inf


def find_max_profit(prices):
  max_profit = -math.inf
  min_value = prices[0]

  for price in prices:
    max_profit = max(max_profit, price - min_value) if price != min_value else max_profit
    min_value = price if price < min_value else min_value
    if debug:
      print(f"max_profit: {max_profit}, min_value: {min_value}")

  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))