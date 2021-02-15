import copy
import random
# Consider using the modules imported above.
# reference to / thanks for experiment() code - 
# https://repl.it/@paulboehnke/boilerplate-probability-calculator-2#prob_calculator.py

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    
    if len(kwargs) == 0: 
      return None

    for key, arg in kwargs.items():
      self.contents.extend([key]*int(arg))

    #print(self.contents)

  def draw(self, to_draw):
    balls_drawn = []
    
    if (to_draw >= len(self.contents)):
      balls_drawn = self.contents
      self.contents = []
    else:
      for i in range(to_draw):
        random.shuffle(self.contents)
        balls_drawn.append(self.contents.pop())
    #print(balls_drawn)
    return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_hits = 0

  for i in range(num_experiments):
    balls_drawn = copy.deepcopy(hat).draw(num_balls_drawn)
    print(balls_drawn)
    found = True
    for expected_ball, count in expected_balls.items():
      if balls_drawn.count(expected_ball) < count: 
        found = False
        #print(found)
        break
            
    if found: num_hits+=1
        
  return num_hits/num_experiments
