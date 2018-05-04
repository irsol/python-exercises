def fibo(num):
    n1 = 0
    n2 = 1
    result = [0]
    print("Fibonacci sequence: ")

    for n in range(2, num):
        n3 = n1 + n2
        result.append(n2)
        n1 = n2
        n2 = n3
    print(result)
    #return

fibo(5)