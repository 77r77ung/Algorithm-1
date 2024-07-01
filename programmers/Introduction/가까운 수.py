'''
정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
'''
def solution(array, n):
    array.append(n)
    array.sort()
    for i in range(1, len(array)):
        if array[i] == n:
            if i == len(array)-1:
                return array[i-1]
            if abs(n-array[i-1]) <= abs(n-array[i+1]):
                return array[i-1]
            else:
                return array[i+1]

'''
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]
'''