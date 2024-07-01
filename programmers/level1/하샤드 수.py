'''
하샤드 수

양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
'''

# array = []

# temp = int(input())
# for _ in str(temp):
#     array.append(int(_))

# sum = 0
# for i in array:
#     sum += i

# if (temp%sum == 0):
#     print('t')
# else:
#     print('f')

def solution(x):
    array = []
    answer = True
    n_answer = False
    
    for _ in str(x):
        array.append(int(_))

    sum = 0
    for i in array:
        sum += i

    if (x%sum == 0):
        return answer
    else:
        return n_answer

print(solution(10))

'''
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
'''

# n = 'hi'
# for c in str(n):
#     print(c)