import re

def arithmetic_arranger(problems, calculate="False"):
  arranged_problems = ""
  upper_line = ""
  lower_line = ""
  dash_line = ""
  result_line = ""

  # print(calculate)
  
  if len(problems) > 5:
    return "Error: Too many problems."
  
  for x in problems:
    n1, op, n2 = x.split()
    #print(n1, op, n2)
    
    if op != "+" and op != "-":
      return "Error: Operator must be '+' or '-'."
    
    if not n1.isdigit() or not n2.isdigit(): 
      return "Error: Numbers must only contain digits."

    if len(n1) > 4 or len(n2) > 4:
      return "Error: Numbers cannot be more than four digits."

    if op == "+":
      sum = str(int(n1) + int(n2))
    else:
      sum = str(int(n1) - int(n2))

    length = max(len(n1), len(n2))
    upper_line += str(n1.rjust(length + 2)) + "    "
    lower_line += str(op + " " + n2.rjust(length)) + "    "
    dash_line += str("-" * (length + 2)) + "    "
    result_line += str(sum).rjust(length + 2) + "    "
      
  if calculate:
    arranged_problems += upper_line + "\n" + lower_line + "\n" + dash_line + "\n" + result_line
  else:
    arranged_problems += upper_line + "\n" + lower_line + "\n" + dash_line

  return arranged_problems

    #print(x)
    #if re.search("\*", x) or re.search("\/", x):
    #  print("wrong op")
    #  return "Error: Operator must be '+' or '-'."
    #if re.search("\D", x):
    #  print("not digits")
    #  return "Error: Numbers must only contain digits."
    
    #numbers = re.findall("\d", x)
    #if numbers:
    #  print(numbers)

      
  return arranged_problems
