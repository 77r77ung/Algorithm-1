'''
선분 3개가 평행하게 놓여 있습니다.
세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때,
두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.
lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.
선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.
'''
from collections import defaultdict
def solution(lines):
    countHash = defaultdict(int)
    dots = []
    
    # 모든 점들을 기준 선분의 길이가 1이 되도록 쪼개기
    for _ in lines:
        for i in range(_[0], _[1]):
            countHash[(i, i+1)] += 1
            # dots.append([i, i+1])
    
    count = 0
    for key, value in countHash.items():
        if value >= 2:
            count += 1
            
    return count