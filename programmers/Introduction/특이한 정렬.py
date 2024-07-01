'''
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다.
이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다.
정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.
'''
from collections import defaultdict
def solution(numlist, n):
    diffHash = defaultdict(set)
    
    # 배열원소: n - 배열 원소 (차이를 비교하기 위해서)
    # sorted(numlist): 반례(testcase3)를 해결하기 위해서
    for _ in sorted(numlist):
        diffHash[_] = abs(n-_)
    
    # n-배열 원소가 작은 것 순으로 정렬
    # reverse = True를 하면 n-배열 원소가 같을 때는 큰 원소 먼저 코드를 굳이 구현하지 않아도 됨
    newHash = sorted(diffHash.items(), key = lambda item:item[1], reverse = True)
    
    # newHash를 다시 뒤집어서 배열 형태로 정렬!
    result = []
    for _ in newHash[::-1]:
        result.append(_[0])
    return result