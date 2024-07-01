'''
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

* enumerate() : for문에서 사용할 수 있음(인덱스, 값 모두 출력 가능)
  .split() vs .split(" ") 차이점
'''
def solution(s):
    answer = ''
    for _ in s.split(' '):
        for i, j in enumerate(_):
            if i % 2 == 0:
                answer += j.upper()
            else:
                answer += j.lower()
        answer += " "
    return answer[:-1]
    
'''
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
'''