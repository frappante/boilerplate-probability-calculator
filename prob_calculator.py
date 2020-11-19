import copy
import random

# Hat contains set of balls per colour, added to a list called contents.
class Hat:

  contents = []

  def __init__(self, **colours):
    
    self.contents = []
    self.colours = colours

    for k, v in self.colours.items():
      for z in range(v):
        self.contents.append(k)   

  
  # Draws n balls from a hat at random, without replacement
  def draw(self, n):
    
    output = []
   
    if len(self.contents) >= n:
      out = random.sample(self.contents, n)
      for x in out:
        self.contents.remove(x)
      return out
    else:
      return self.contents
      

# Calculates a rough probability of drawing the expected balls out of a hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  output = []
  match = 0
  probability = 0
  colour = ""

  
  for i in range(num_experiments):
    h = copy.deepcopy(hat)
    output = h.draw(num_balls_drawn)


    # drawn is new dictionary for selected balls
    
    drawn = {}
    for colour in output:
      drawn[colour] = drawn.get(colour, 0) + 1

    # check if expected balls are drawn each time

    m = 0
    for k, v in expected_balls.items():   
      if k in drawn and expected_balls[k] <= drawn[k]:
        m += 1
      else:
        m = m        


    if m == len(expected_balls):
      match += 1   

  probability = match / num_experiments
  return probability