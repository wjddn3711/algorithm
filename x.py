reg = ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"]
new = "cow"

def sol(reg, new):
    if new not in reg:
        return new

    # 만약 중복되는 아이디가 있다면
    N = ''
    S = ''
    for i in range(len(new)):
        if new[i].isdigit(): # 만약 숫자라면
            N+=new[i]
        else: # 문자라면
            S+=new[i]
    if N=='':
        N='0'
    new = S+str(int(N)+1)
    return sol(reg,new) # 재귀적으로 중복되지 않을때까지 +1 해주며 호출

print(sol(reg,new))

