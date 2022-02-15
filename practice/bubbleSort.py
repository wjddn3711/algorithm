l = [5,4,3,1,9,7]

for i in range(len(l)-1):
    swap = False
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
            swap = True
    if not swap:
        break


print(l)