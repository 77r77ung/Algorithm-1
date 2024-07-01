'''
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다.
"z"는 1만큼 밀면 "a"가 됩니다.
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
'''
from string import ascii_lowercase, ascii_uppercase
def solution(s, n):
    l_alphabet, u_alphabet = list(ascii_lowercase)*2, list(ascii_uppercase)*2
    
    answer = []
    for _ in s:
        if _.isupper():
            answer.append(u_alphabet[u_alphabet.index(_)+n])
        elif _.islower():
            answer.append(l_alphabet[l_alphabet.index(_)+n])
        else:
            answer.append(" ")
    return "".join(answer)