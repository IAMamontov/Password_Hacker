def fibonacci(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        if i <= 1:
            yield i
        else:
            f = f2 + f1
            f1 = f2
            f2 = f
            yield f