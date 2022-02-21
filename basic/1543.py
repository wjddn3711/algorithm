
exam = input()
target = input()
cnt = 0
tl = len(target)
cut = 0
while len(exam)-cut >= tl:
    if exam[cut:cut+tl] == target:
        cut = cut+tl
        cnt+=1
    else:
        cut +=1
print(cnt)
