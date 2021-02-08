from replit import clear
from art import logo

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

operations = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div,
}

while True:
  print(logo)
  num1 = float(input("What's your first number? : "))
  for symbol in operations:
    print(f"{symbol}")

  continue_calculation = True;
  while continue_calculation:
    op_symbol  = input("Pick an operation : ")
    operation_function = operations[op_symbol]
    num2 = float(input("What's the next nummber? :"))
    result = operation_function(num1,num2)
    print(f"{num1} {op_symbol} {num2} = {result}")
    if input(f"'y' to continue calculating with {result} or 'n' to start new calculation : ")=="y" :
      num1 = result
      continue_calculation = True
    else : 
      continue_calculation = False

  clear()
