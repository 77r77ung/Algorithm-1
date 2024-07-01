'''
문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
예를 들어, s="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.
최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.
문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.
'''
def solution(s):
    result = []
    for _ in range(len(s)):
        if s[_] in s[:_]:
            while s[:_].count(s[_]) > 1:
                s = s.replace(s[_], '0', 1)
            result.append(_-s.index(s[_]))
        else:
            result.append(-1)
    return result