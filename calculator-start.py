from replit import clear
from art import logo


def add(n1, n2):
  return n1 + n2


def subtraction(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def division(n1, n2):
  return n1 / n2


operations = {"+": add, "-": subtraction, "*": multiply, "/": division}


def calculator():
  print(logo)
  continue_calc = True
  num1 = float(input("What's the first number?\n "))
  while continue_calc == True:

    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an Operation from above:")
    calculation = operations[operation_symbol]
    num2 = float(input("What's the second number?\n "))
    answer = float("{:.2f}".format(calculation(num1, num2)))
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    ask = input(
        f"Do you want to continue?Type 'y' to continue calculating {answer} with  and 'n' to stop the calculation or 'r' for new calculation:\n"
    )
    if ask == "y":
      num1 = answer

    elif ask == "n":
      continue_calc = False
      
      print("\nThank You!")
      break
    else:
      clear()
      calculator()


calculator()
