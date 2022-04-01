from itertools import combinations as cb
def solution(number, k):
    '''
    # combinations 를 활용하여 푸는 경우 (시간초과)

    result = '0'
    # 1,9,2,4 중에 len(number)-k 만큼 뽑아 조합하였을때 가장 큰수를 반환
    for n in cb(number,len(number)-k):
        result = max(result,''.join(n))
    return result
    '''
    answer = [] # Stack

    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)
    