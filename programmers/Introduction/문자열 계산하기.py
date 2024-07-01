'''
my_string은 "3 + 5"처럼 문자열로 된 수식입니다.
문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
'''
def solution(my_string):
    arr = my_string.split(" ")
    answer = int(arr[0])
    for _ in range(0, len(arr)):
        if _ % 2 != 0:
            if arr[_] == '+':
                answer += int(arr[_+1])
            else:
                answer -= int(arr[_+1])
    return answer

'''
solution=eval
'''
