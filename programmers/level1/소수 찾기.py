'''
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
'''
def solution(n):
    result = []
    # array를 True로 설정하는 이유?
    array = [True for _ in range(n+1)]
    
    # n**0.5: 루트 n / 루트 n보다 작은 소수들로 나누어 떨어지지 않으면 n은 소수임.
    for i in range(2, int(n**0.5)+1):
        # 처리하지 않은 가장 작은 수(True인 수) i 탐색
        if array[i] == True:
            j = 2
            while i * j <= n:
                # i의 배수 모두 제거
                array[i*j] = False
                j += 1
    
    for i in range(2, n+1):
        # array[i]가 True이면(= 소수이면)
        if array[i]:
            result.append(i)
            
    return len(result)

'''
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''