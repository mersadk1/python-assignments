import random

index = 0
array = []
n = int(input("enter the length of the list (from 1 to 1000): "))

while True:
    if index != n:
        number = random.randint(1,1000)
        if index == 0:
            array.append(number)
            index += 1
        else:
            for i in range(len(array)):
                if number != array[i]:
                    if i == len(array) - 1:
                        array.append(number)
                        index += 1
                    else:
                        continue
                else:
                    continue
    else:
        break
    
print(array)
