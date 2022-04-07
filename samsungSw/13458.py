'''
총 N개의 시험장이 있고, 각각의 시험장마다 응시자들이 있다. i번 시험장에 있는 응시자의 수는 Ai명이다.
감독관은 총감독관과 부감독관으로 두 종류가 있다.
총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명이고,
부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명이다.
각각의 시험장에 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 있어도 된다.
'''

n = int(input())
A = list(map(int,input().split()))
A.sort()
b,c = map(int,input().split())

'''
각 시험장당 총 시험관은 1명 부는 여러명이 가능하다
각 시험장들을 내림차순으로 정렬하여 처음에 총시험관을 넣고 남는 곳에 부시험관을 배치하도록 한다
'''
cnt = 0
for place in A:
    cnt+=1 # 항상 총감독관이 존재해야한다
    place -= b
    if place <= 0: continue
    if place/c > 0:
        if place%c == 0:
            cnt+= place//c
        else:
            cnt+= place//c +1
    else:
        cnt+=1

print(cnt)