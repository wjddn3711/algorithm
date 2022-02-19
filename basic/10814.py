t = int(input())
member = [list(input().split())+[i] for i in range(t)]
print(member)
member.sort(key=lambda x:(int(x[0]),x[2]))
[print(x,y) for x,y,z in member]