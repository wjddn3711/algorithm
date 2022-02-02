
def rotation(n):
    # print(n)
    if n == 1:
        return n
    if n%2==0: #짝수라면
        return rotation(n//2)
    else:
        return rotation(3*n+1)

rotation(3)


def combi(n):
    if n == 1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return combi(n-3)+combi(n-2)+combi(n-1)

print(combi(5))