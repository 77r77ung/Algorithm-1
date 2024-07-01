'''
핸드폰 번호 가리기

프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
'''

# def solution(phone_number):
#     answer = ''
#     arr = []
    
#     for i in str(phone_number): arr.append(i)
#     arr.reverse()
    
#     for j in range(len(arr)):
#         if j >= 4:
#             arr[j] = '*'
#     arr.reverse()
    
#     answer = ''.join(arr)
    
#     return answer

# print(solution('01012345678'))
# print(solution('010123456'))

'''
phone_number = input()
arr = []

for i in str(phone_number):
    arr.append(i)

arr.reverse()

for j in range(len(arr)):
    if j >= 4:
        arr[j] = '*'

arr.reverse()

answer = ''.join(arr)
print(answer)
'''


# s = '01012345678'
# print(len(s)) > 11
# print(len(s)-4) > 7
# print(s[-4:]) > 5678

# '*' * (len(s) - 4) + s[-4:]