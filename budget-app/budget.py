class Category:

# thanks to some code. - https://repl.it/@natalieparent9/boilerplate-budget-app-1#test_module.py
# from @natalieparent9

  def __init__(self, name):
    self.name = name
    self.total_cat_spend = 0
    self.ledger = []
  
  def __str__(self):
      #print_str = ""
      #for i in range(len(self.ledger)):
      #  print_str += self.ledger[i]['description'][:23] + ' '*(30 - len(self.ledger[i]['description'][:23]) - len(str('{0:.2f}'.format(self.ledger[i]['amount'])))) + str('{0:.2f}'.format(self.ledger[i]['amount']))+"\n"
      #funds = 'Total: ' + str(self.get_balance())
      #return "*"*int((30 - (len(self.name))) / 2) + self.name + "*"*int((30 - (len(self.name))) / 2)+'\n' + print_str + funds
    
    objec = (self.name.center(30, "*") + "\n")
    for entry in self.ledger:
      objec = objec + f"{entry['description'][0:23].ljust(23)}{format(entry['amount'],'.2f').rjust(7)}\n"
    objec = objec + f"Total: {format(self.get_balance(), '.2f')}"
    return objec

  def deposit(self, deposit_amount, description=""):
    self.ledger.append({"amount": deposit_amount, "description": description})

  def check_funds(self, amount):
    working_funds = 0
    for i in range(len(self.ledger)):
      working_funds += self.ledger[i]["amount"]
    if (working_funds >= amount):
      return True
    else:
      return False

  def withdraw(self, withdraw_amount, description=""):
    if self.check_funds(withdraw_amount):
      self.ledger.append({"amount": -withdraw_amount, "description": description})
      self.total_cat_spend += withdraw_amount
      return True  
    else:
      return False         

  def get_balance(self):
    working_funds = 0
    for i in range(len(self.ledger)):
      working_funds += self.ledger[i]["amount"]
    return working_funds

  def transfer(self, amount, category):
    if(self.withdraw(amount, "Transfer to " + category.name)):
        category.deposit(amount, "Transfer from " + self.name)
        return True
    return False

def create_spend_chart(categories):
  bar_chart = "Percentage spent by category\n"
  total_spend = 0
  spend_bycategory = {}
  percentages_bycategory = {}
  name_length = 0

  for category in categories:
    spend_bycategory[category.name] = category.total_cat_spend
    total_spend += category.total_cat_spend
    #print("cat spend", category.total_cat_spend)
  #print(spend_bycategory)

  for name, total_cat_spend in spend_bycategory.items(): 
      percent = total_cat_spend / total_spend * 100
      percent = percent - (percent % 10)
      percentages_bycategory[name] = percent
      # print(name, percentages_bycategory[name])
  #print(percentages_bycategory)
  #print("total spend", total_spend)

# create the y axis and add the values to the chart
  x = 100
  for number in range(11):
    bar_row = f"{x}".rjust(3) + "| "
    for name, percent in percentages_bycategory.items():
      if percent >= (x):
        bar_row += "o  "
      else:
        bar_row += "   "
    bar_chart += bar_row + '\n'
    x -= 10
   
# add the x axis
  x_axis = "    -"
  for category in categories:
    x_axis += ("---")
  bar_chart += x_axis + "\n"

# determines the longest category name length
  for category in categories:
    if len(category.name) > name_length:
      name_length = len(category.name)
 
# add the category names for x axis values
  y = 0
  while y <= name_length:
    row = "     "
    for key, value in percentages_bycategory.items(): 
      category_name = key
      try:    
        row +=  category_name[y] + "  "
      except: # for when the name has already been spelled out
        row += "   "
        
    if y <= name_length - 1:
      bar_chart += row + '\n' 
    else:
      bar_chart += row.strip(" ")               
    y += 1
  
  bar_chart = bar_chart.rstrip("\n")
  return bar_chart
