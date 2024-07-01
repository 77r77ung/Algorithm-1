'''
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

* sum을 이용해 한 줄 코드 작성해보기
'''

def solution(n):
    hap = 0
    for _ in range(1, n+1):
        if n%_ == 0:
            hap += _
    return hap