def fib_iter(n):
    if n <= 1: #pravi proverka za purvite 2 sluchaq
        return n
    a, b = 0, 1
    for _ in range(n - 1): #ciku za izchislenie 
        a, b = b, a + b
    return b
