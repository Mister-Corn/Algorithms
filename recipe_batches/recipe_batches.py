#!/usr/bin/python

import math

"""
Approach is to loop though each key in one of the objects, then
use the key to get the number of ingredients required and on hand
from both objects. If a key in `recipe` doesn't exist in `ingredients`,
we don't have a required ingredient on hand, and therefore cannot
make any batches. In that case, set `max_batches` to 0, and break.

From there, divide the qty. on hand over qty. required, then round 
down (unless you're cool with making 0.39781 of a cake). Save the 
result to `max_batches` variable if the value of the result is less
than the current value in `max_batches`.

As a little optimization, have the loop stop if ever `batches == 0`. 
The result can go no lower than that, so it is uneccesary to check 
further keys if there are any.
"""

def recipe_batches(recipe, ingredients):
  max_batches = math.inf

  for ingredient in recipe: # `milk` `butter` `flour`
    if ingredient in ingredients:
      # Apparently, typecasting a float into an int rounds it down
      # https://stackoverflow.com/a/17142719
      # `math.floor` is another alternative
      batches = int(ingredients[ingredient] / recipe[ingredient])
      max_batches = batches if batches < max_batches else max_batches
      if not batches: # 0, "", false, 
        break
    else:
      # We don't have an ingredient on hand, so we can't make any batches
      max_batches = 0
      break

  return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))