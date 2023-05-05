import math
import time

condition = 1

print("welcome to calculator app :D \n")
time.sleep(2)



while condition:
    
    string = input("enter the desired operation : ").split(" ")

    if len(string) == 3:
        n1 , op , n2 = int(string[0]) , string[1] , int(string[2])
        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            result = int(n1 / n2)
    else:
        op , n1 = string[0] , int(string[1])
        if op == "sin":
            result = math.sin(n1)
        elif op == "cos":
            result = math.cos(n1)
        elif op == "tan":
            result = math.tan(n1)
        elif op == "cot":
            result = math.cos(n1)/math.sin(n1)
        elif op == "factorial":
            result = math.factorial(n1)
        elif op == "radical":
            result = int(math.sqrt(n1))

    print("the result is : " , result)

    qst = input("\ndo you want to continue the calculation? (YES/NO) ")
    if qst == "NO":
        condition = 0
    else:
        print("\n \n")
        continue
    
