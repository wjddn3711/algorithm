n= int(input())
a = set(map(int,input().split()))
m = int(input())
target = list(map(int, input().split()))
for t in target:
    if t in a:
        print(1)
    else:
        print(0)