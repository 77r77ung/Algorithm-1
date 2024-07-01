'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.
각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.
'''
def solution(arr, queries):
    result = []
    for query in queries:
        temp = arr[query[0]:query[1]+1]
        #print("temp: ", temp)
        temp2 = []
        for i in sorted(temp):
            if i > query[2]:
                temp2.append(i)
                #print("temp2: ", temp2)
        if len(temp2) != 0:
            result.append(temp2[0])
        else:
            result.append(-1)
        #print(result)
    return result