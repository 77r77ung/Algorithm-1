'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
'''
# (tip) i는 index를 의미. arr[i]와 다름.
def solution(arr, queries):
    for s, e, k in queries:
        for index, value in enumerate(arr[s:e+1]):
            '''
            (tip) s+index인 이유: s가 0이 아닌 경우를 고려
            만약 s = 2인데 index로만 계산을 하게 되면
            (index는 0부터 시작하기 때문에) 원하는 값을 도출할 수 없음.
            '''
            if s+index % k == 0:
                arr[s+index] = value+1
    return arr