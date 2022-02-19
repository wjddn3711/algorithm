def fib(n):
    d = [0]*10000
    d[1]=1
    d[2]=1
    for i in range(3,len(d)):
        d[i] = d[i-2]+d[i-1]
    return d[n]

def fib2(n):
    if n<=2:
        return 1
    else:
        return fib2(n-1)+fib2(n-2)

print(fib2(100))