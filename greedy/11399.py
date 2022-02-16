'''
1 2 3 3 4
1 3 6 9 13

'''

def atm(data):
    data.sort()
    for i in range(1, N):
        data[i] += data[i-1]
    print(data)
    return sum(data)

N= int(input())
data = list(map(int, input().split()))
print(atm(data))