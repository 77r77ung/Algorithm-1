'''
직사각형 별찍기

이 문제에는 표준 입력으로 두 개의 정수 n, m이 주어짐.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력.
'''

def solution1(n, m):
    for i in range(m):
        print('*'*n)

n, m = map(int, input().split())
solution1(n, m)