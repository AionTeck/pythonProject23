firstNum = int(input("Enter the first num: "))
secondNum = int(input("Enter the second num: "))
actiom = input("Enter what action to do: ")

def arithmetic(firstNum, secondNum, action):
    if action == "+":
        print(firstNum + secondNum)
    elif action == "-":
        print(firstNum - secondNum)
    elif action == "*":
        print(firstNum * secondNum)
    elif action == "/":
        print(firstNum / secondNum)
    else:
        print('Enter an error action')

arithmetic(firstNum, secondNum, actiom)

