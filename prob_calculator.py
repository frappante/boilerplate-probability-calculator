import copy
import random
# Consider using the modules imported above.

class Hat:

  contents = []

  def __init__(self, **kwargs):
    
    self.contents = []
    self.kwargs = kwargs

    for k, v in self.kwargs.items():
      for z in range(v):
        self.contents.append(k)   


  def draw(self, n):
    
    output = []
   
    if len(self.contents) >= n:
      for i in range(n):
        ball = random.choice(self.contents)
        output.append(ball)
        self.contents.remove(ball)
        #self.contents.pop(self.contents.index(ball))
      return output
    else:
      return self.contents


    self.drawnum = n
    if len(self.contents) >= self.drawnum:
      out = random.sample(self.contents, self.drawnum)
      for x in out:
        self.contents.remove(x)
      return out
      


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