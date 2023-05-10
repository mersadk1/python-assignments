def fibo(n):
    array = []
    a1 = 0
    a2 = 1
    for i in range(n):
        if i == 0:
            array.append(a2)
        else:
            array.append(a2 + a1)
            a1 = a2
            a2 = array[i]
    array = array[::-1]
    print(array)
        
n = int(input("enter n : "))
fibo(n)