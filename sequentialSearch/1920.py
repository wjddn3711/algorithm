
def binary(data, start, end,target):
    if start>end:
        return 0
    mid = (start+end)//2 # 중간값 받기
    if target==data[mid]:
        return 1
    if target > data[mid]:
        # 타겟이 중간값보다 크다면 data의 뒤부분
        return binary(data, mid+1,end, target)
    else:
        return binary(data, start,mid-1,target)

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
targets = list(map(int,input().split()))
for t in targets:
    print(binary(A,0,N-1,t))

