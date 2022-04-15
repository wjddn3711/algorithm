from itertools import combinations
'''
길이가 N인 수열 A1, A2, ..., AN이 주어진다. 이때, 1 ≤ i < j < k ≤ N 이면서,
Aj - Ai = Ak - Aj를 만족하는 (i, j, k) 쌍의 개수를 구하는 프로그램을 작성하시오.
'''
result = 0
n= int(input())
A = list(map(int,input().split()))
for combi in combinations(A,3):
    i,j,k = combi
    if j-i == k-j:
        result+=1
print(result)
