'''
평균 구하기

정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
'''

def solution(arr):
    hap = 0

    for i in arr:
        hap += i

    return (hap / len(arr))

print(solution([1, 2, 3, 4]))
# print(solution([5, 5]))

'''
def average(list):
    return (sum(list) / len(list))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));

'''