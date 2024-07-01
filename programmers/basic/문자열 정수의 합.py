'''
한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_str):
    array = []
    for _ in num_str:
        array.append(int(_))
    return sum(array)

'''
def solution(num_str):
    return sum(map(int, list(num_str)))
'''