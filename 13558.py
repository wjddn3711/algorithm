'''
길이가 N인 수열 A1, A2, ..., AN이 주어진다. 이때, 1 ≤ i < j < k ≤ N 이면서,
Aj - Ai = Ak - Aj를 만족하는 (i, j, k) 쌍의 개수를 구하는 프로그램을 작성하시오.
'''

n= int(input())
A = list(map(int,input().split()))

answer = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            if A[j]-A[i]==A[k]-A[j]:
                answer+=1

print(answer)