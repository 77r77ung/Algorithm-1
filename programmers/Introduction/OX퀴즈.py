'''
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다.
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(quiz):
    answer = [ [i for i in _.split(" ")] for _ in quiz]
    print(answer)
    result = []
    for _ in range(len(answer)):
        if answer[_][1] == '+':
            if int(answer[_][0]) + int(answer[_][2]) == int(answer[_][4]):
                result.append("O")
            else:
                result.append("X")
        if answer[_][1] == '-':
            if int(answer[_][0]) - int(answer[_][2]) == int(answer[_][4]):
                result.append("O")
            else:
                result.append("X")
    return result

'''
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]   
'''