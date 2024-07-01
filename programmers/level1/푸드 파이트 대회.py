'''
수웅이가 준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열 food가 주어졌을 때,
대회를 위한 음식의 배치를 나타내는 문자열을 return 하는 solution 함수를 완성해주세요.
'''
def solution(food):
    result = [str(_)*(food[_]//2) for _ in range(1, len(food)) if food[_] >= 2]
    return "".join(result) + "0" + "".join(result)[::-1]