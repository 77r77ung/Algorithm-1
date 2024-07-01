'''
첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다.
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''

# 유클리드 호제법을 이용한 최대공약수 구하기
def GCD(x, y):
    # y가 참일 경우(즉, y가 자연수일 때) | (y) ==> (x%y != 0) 변경 가능
    while(y):
        # x -> y 대입, y -> x%y(=r) 대입
        x, y = y, x%y
    return x

# print(GCD(6, 29))

import math
def solution(denum1, num1, denum2, num2):
    denum = denum1*num2 + denum2*num1
    num = num1 * num2
    
    return [denum//math.gcd(denum, num), num//math.gcd(denum, num)]