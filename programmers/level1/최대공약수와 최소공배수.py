'''
최대공약수와 최소공배수

두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
'''
# 1. min, max 구분하기 -> 굳이 필요 없음!
# 2. 유클리드 호제법
# 3. (n * m) / GCD

def GCD(n, m):
    if n>m:
        max = n
        min = m
    else:
        max = m
        min = n
    return min if max%min == 0 else GCD(max%min, min)

def LCM(n, m):
    return int((n*m) / GCD(n, m))

def solution(n, m):
    return [GCD(n, m), LCM(n, m)]

# print(solution(3, 12))

'''
# lambda 함수를 사용하는 방법
def solution(n, m):
    GCD = lambda a,b : b if not a%b else GCD(b, a%b)
    LCM = lambda a,b : a*b // GCD(a, b)

# if not a%b -> a%b(=1)이 not(아니라면) == 0이라면 b 반환 ... else ~~
# // 연산자: 나눗셈에서 소수점 버리고 출력 (== float -> int)
'''

'''
n = 3
m = 12
max_n = []
max_m = []
min_n = []
min_m = []
gop = 1
j = 1
y = 1

for i in range(1, n+1):
    if (n%i) == 0:
        max_n.append(i)
        i += 1
while True:
    gop = j*n
    min_n.append(gop)
    j += 1
    if gop >= 100:
        break
    

for x in range(1, m+1):
    if (m%x) == 0:
        max_m.append(x)
        x += 1
while True:
    gop = y*m
    min_m.append(gop)
    y += 1
    if gop >= 100:
        break

print(max_n)
print(min_n)
print(max_m)
print(min_m)
'''
