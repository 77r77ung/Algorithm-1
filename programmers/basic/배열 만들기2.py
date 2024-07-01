'''
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.
'''
def solution(l, r):
    result = []
    for i in range(l, r+1):
        # if all: list 값이 조건에 모두 만족해야 실행된다.
        '''
        c in 문자열: c가 문자열에 포함되어 있는지 확인한다.
            - 반환값: True/False 반환
        c not in 문자열: c가 문자열에 포함되어 있지 않은지 확인한다.
            - 반환값: True/False 반환
        문자열.find(c): c가 문자열에 포함되어 있는지 확인한다.
            - 반환값: c가 문자열에 어디에 위치하고 있는지 index를 int형으로 반환
        
        '''
        if all(num in ['0', '5'] for num in str(i)):
            result.append(i)
    if len(result) == 0:
        result.append(-1)
    return result