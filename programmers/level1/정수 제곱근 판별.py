'''
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고,
n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
'''
def solution(n):
    gop2 = n ** (1/2)
    return (gop2+1)**2 if gop2 % 1 == 0 else -1
# print(solution(121))
# print(solution(3))

'''
# -1이 계속 출력되다가 i == 11일 때, i를 제대로 출력함.
for i in range(1, 122):
    if i == 121**(1/2):
        print(i)
    else:
        print(-1)

-> 양의 정수라는 조건식이 하나 더 필요함!
'''