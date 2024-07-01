'''
정수가 담긴 리스트 num_list가 주어질 때,
num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(num_list):
    jcount = 0
    hcount = 0
    answer = []
    for _ in num_list:
        if _ % 2 == 0:
            jcount += 1
        else:
            hcount += 1
    answer.append(jcount)
    answer.append(hcount)
    return answer