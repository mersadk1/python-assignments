import random
import time


condition = 1

print("hey! let's play a game ")
time.sleep(1.5)
print("are you ready!?")
time.sleep(2)

while condition:
    
    print("1")
    time.sleep(0.8)
    print("2")
    time.sleep(0.8)
    print("3")
    time.sleep(1)
    
    num = random.randint(1,6)
    
    if num == 6:
        print("WOW!! number 6 , You have one more chance :D")
        time.sleep(3)
        print("are you ready again??")
        time.sleep(2)
        continue
    else:
        print("you rolled number" , num)
        condition = 0
    
