def selectionSort(ar):
    for i in range(len(ar)-1):
        maxI = i
        for j in range(i+1,len(ar)):
            if ar[j] > ar[maxI]:
                maxI = j
        ar[i],ar[maxI] = ar[maxI],ar[i]
    return ar

nums = input()
target = []
for i in range(len(nums)):
    target.append(int(nums[i]))
answer = selectionSort(target)
for a in answer:
    print(a,end='')