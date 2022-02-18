t = int(input())
for i in range(t):
    pw = []
    dummy = []
    log = input()
    # 커서를 기준으로 두 스택을 이용하여 처리
    # 문자일때는 왼쪽 스택에 삽입
    # < 일때는 왼쪽에서 오른쪽으로 삽입
    # > 일때는 오른쪽에서 왼쪽으로 삽입
    for char in log:
        if char =='<' :
            if pw:
                dummy.append(pw.pop())
        elif char =='>':
            if dummy:
                pw.append(dummy.pop())
        elif char =='-':
            pw.pop()
        else:
            pw.append(char)
    pw.extend(reversed(dummy))
    print(''.join(pw))


test_cases = int(input())

