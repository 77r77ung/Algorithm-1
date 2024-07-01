'''
두 정수 left와 right가 매개변수로 주어집니다.
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
'''
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        temp = set()
        for j in range(1, i+1):
            if i % j == 0:
                temp.add(j)
        if len(temp) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

'''
// 약수가 홀수개인 모든 수는 제곱수이다.
// i의 제곱근 구하기: i ** 0.5
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''