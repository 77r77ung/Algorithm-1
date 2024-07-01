'''
3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다.
3x 마을 사람들의 숫자는 다음과 같습니다.
정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    num_list = []
    for i in range(1, 200):
        if i % 3 == 0 or "3" in str(i):
            pass
        else:
            num_list.append(i)
    # print(num_list)
    return num_list[n-1]

'''
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
'''