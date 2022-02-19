
def solve(size,x,y):
    global result
    if size==2:
        # 1사 분면이며 좌표가 같다면 result 프린트
        if x==r and y==c:
            print(result)
            return
        result+=1
        if x==r and c==y+1:
            print(result)
            return
        result+=1
        if r==x+1 and c==y:
            print(result)
            return
        result+=1
        if r==x+1 and c==y+1:
            print(result)
            return
        result+=1
        return
    solve(size//2,x,y)
    solve(size//2,x,y+size//2)
    solve(size//2,x+size//2,y)
    solve(size//2,x+size//2,y+size//2)

result=0
n,r,c = map(int, input().split())
solve(2**n,0,0)