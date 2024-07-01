'''
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요. 
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
'''
def solution(a, b):
    if a > b:
        return sum(int(i) for i in range(b, a+1))
    else:
        return sum(int(i) for i in range(a, b+1))

'''
* a, b = b, a로 두 변수의 값을 도치할 수 있음.
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
'''