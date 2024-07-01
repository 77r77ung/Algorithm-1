'''
행렬의 덧셈

행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

'''

def solution(arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        temp = []
        for x, y in zip(i, j):
            temp.append(x+y)
        answer.append(temp)

    return answer
print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))

# '''
# arr1 = [[1, 2], [2, 3]]
# arr2 = [[3, 4], [5, 6]]
# answer = []

# for i in range(len(arr1)):
#     temp = []
#     for j in range(len(arr1[0])):
#         temp.append(arr1[i][j] + arr2[i][j])
#     answer.append(temp)

# print(answer)
# '''

# arr1 = [[1, 2], [2, 3]]
# arr2 = [[3, 4], [5, 6]]
# answer = []
# for i, j in zip(arr1, arr2):
#     for x, y in zip(i, j):
#         temp = []
#         # print(x)
#         # print(y)
#         temp.append(x+y)
#         print("temp = ")
#         print(temp)
#         answer.append(temp)
#         print("answer = ")
#         print(answer)
    

    