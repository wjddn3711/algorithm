from itertools import product


# result = 0
# def solve(result,end,sol):
#     if end==r:
#         if eval(result) == 0:
#             print(sol)
#             return
#     else:
#         solve(result+str(end+1),end+1,sol+(' '+str(end+1)))
#         solve(result+('+'+str(end+1)),end+1,sol+('+'+str(end+1)))
#         solve(result+('-'+str(end+1)),end+1,sol+('-'+str(end+1)))

import copy
op= []
ar = []
def expressions(ar,n):
    if len(ar)==n:
        op.append(copy.deepcopy(ar))
        return

    ar.append(' ')
    expressions(ar,n)
    ar.pop()

    ar.append('+')
    expressions(ar,n)
    ar.pop()

    ar.append('-')
    expressions(ar,n)
    ar.pop()

expressions(ar,5)
print(op)
#
#
# t = int(input())
# for _ in range(t):
#     r = int(input())
#     nums = [i+1 for i in range(r)]
#     # solve('1+2',2,'1+2')
#     # solve('1-2',2,'1-2')
#     # solve('12',2,'1 2')
#     exp = [' ','+','-']
#     prob = list(product(exp,repeat=r-1))
#     for i in range(len(prob)):
#         result = ''
#         for j in range(len(nums)):
#             result += str(nums[j])
#             if j!=r-1:
#                 result+=prob[i][j]
#         if eval(result.replace(' ',''))==0:
#             print(result)



