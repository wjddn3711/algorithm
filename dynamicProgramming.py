
# 피보나치를 재귀로 구현했을때
def fibonacci(n):
    if n<=1: return n
    return fibonacci(n-1)+fibonacci(n-2)

# 동적 계획법으로 했을때
def fibo_dp(num):
    cache = [0 for _ in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, num+1): #0,1 은 이미 계산되어있음
        cache[i] = cache[i-1]+cache[i-2]
    return cache[num]