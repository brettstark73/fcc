import re

def arithmetic_arranger(problems, calculate="False"):
  arranged_problems = problems
  print(calculate)
  
  if len(problems) > 5:
    return "Error: Too many problems."
  
  for x in problems:
    print(x)
    if re.search("\*", x) or re.search("\/", x):
      return "Error: Operator must be '+' or '-'."
    if re.search("\D", x):
      return "Error: Numbers must only contain digits."


      
  return arranged_problems
