import random
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

# print(factorial(4))

def multiple(data):
    if data<=1:
        return 1
    return data*multiple(data-1)

# print(multiple(10))

data = random.sample(range(100),10)
print(data)

def sumAr(ar,curr):
    if curr == 0:
        return ar[curr]
    return ar[curr]+sumAr(ar,curr-1)

print(sum(data))
print (sumAr(data,len(data)-1))

def palindrom(string):
    if len(string) <=1:
        return True

    if string[0]==string[-1]:
        return palindrom(string[1:-1])
    else:
        return False
print(palindrom('rumor'))