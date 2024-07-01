'''
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

입출력 예#1
 > arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다.
   따라서 [5, 10]을 리턴합니다.
입출력 예#2
 > arr의 모든 원소는 1으로 나누어 떨어집니다.
   원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.
입출력 예#3
 > 3, 2, 6은 10으로 나누어 떨어지지 않습니다.
   나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.
'''
def solution(arr, divisor):
    answer = sorted(list(_ for _ in arr if _%divisor == 0))
    return answer if len(answer)!=0 else [-1]

print(solution([5, 9, 7, 10], 5))
print(solution([3, 2, 6], 10))

'''
* return or [-1] 알아보기!

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
'''