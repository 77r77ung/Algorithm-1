'''
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

* lambda 다중 조건은 ()로!
'''
strings = ["sun", "bed", "car"]
n = 1
answer = []

'''
# n에 해당하는 인덱스의 문자 뽑아내기
for _ in strings:
    if _[n] == _[n]:
        for i in _:
            print(_[n])
            print(sorted(strings, key = lambda i : i))
        else:
            print(sorted(strings, key = lambda _ : _[n]))

array = []

for _ in strings:
    if _[n] in _:
        for i in _:
            print('이거임')
            print(sorted(strings, key = lambda i : i))
    else:
        print('저거임')
        print(sorted(strings, key = lambda _ : _[n]))
'''

def solution(strings, n):
    return sorted(strings, key = lambda _ : (_[n], _))
