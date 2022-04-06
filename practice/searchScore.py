answers =[1,3,2,4,2]
answer = []
method1 = [1, 2, 3, 4, 5]
method2 = [2, 1, 2, 3, 2, 4, 2, 5]
method3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
score = [0]*3

idx1,idx2,idx3 = 0,0,0
for i in range(len(answers)):
    idx1 = i%len(method1) if len(method1) <= i else i
    idx2 = i%len(method2) if len(method2) <= i else i
    idx3 = i%len(method3) if len(method3) <= i else i

    if answers[i] == method1[idx1]: score[0]+=1
    if answers[i] == method2[idx2]: score[1]+=1
    if answers[i] == method3[idx3]: score[2]+=1

maxScore = max(score)
for i in range(len(score)):
    if score[i]==maxScore:
        answer.append(i+1)
print(answer)