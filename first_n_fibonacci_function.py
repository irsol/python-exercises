#
# def fibo(num):
#     n1 = 0
#     n2 = 1
#     result = [n1, n2]
#     print("Fibonacci sequence: ")
#
#     for n in range(2, num):
#         n3 = n1 + n2
#         result.append(n3)
#         n1 = n2
#         n2 = n3
#     print(result)
#
# fibo(5)


def fibo(num):
    result = [0, 1]
    print("Fibonacci sequence: ")

    for n in range(2, num):
        n3 = 0 + 1
        result.append(n3)

    print(result)

fibo(5)