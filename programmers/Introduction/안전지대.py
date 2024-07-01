'''
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.
'''
import numpy as np
def solution(board):
    # list index out of range 문제를 해결하기 위해 board의 테두리를 1로 덮어주는 작업
    new_board = np.pad(board, ((1, 1), (1, 1)), constant_values=-1)
    result = np.pad(board, ((1, 1), (1, 1)), constant_values=-1)
    # print(result)
    
    # 폭탄 위치
    bomb = []
    for x in range(0, len(board)+1):
        for y in range(0, len(board)+1):
            if new_board[x][y] == 1:
                bomb.append((x, y))
    # print(bomb)
    
    # 위험 지역을 1로 변경
    for x, y in bomb:
        result[x-1][y-1] = 1
        result[x-1][y] = 1
        result[x-1][y+1] = 1
        result[x][y-1] = 1
        result[x][y] = 1
        result[x][y+1] = 1
        result[x+1][y-1] = 1
        result[x+1][y] = 1
        result[x+1][y+1] = 1
    
    # 안전지대 카운팅
    count = 0
    result_list = result.reshape(1, -1).squeeze()
    for i in result_list:
        if i == 0:
            count += 1
    return count


'''
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

'''