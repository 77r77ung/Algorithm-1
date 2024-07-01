'''
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.
다항식을 계산할 때는 동류항끼리 계산해 정리합니다.
덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때,
동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요.
같은 식이라면 가장 짧은 수식을 return 합니다.
'''

def solution(polynomial):
    # print(polynomial.split(" "))
    answer_int = 0
    array_x = []
    
    for _ in polynomial.split(" ")[::2]:
        if _.isdigit():
            answer_int += int(_)
        elif _ == 'x':
            array_x.append(1)
        else:
            # x항의 계수가 10이상일 때를 고려해 x를 기준으로 쪼개야 함
            for i in _.split('x'):
                if i.isdigit():
                    array_x.append(int(i))
    # print(sum(array_x))
    # print(answer_int)
    
    result = []
    if (sum(array_x)) != 0 and answer_int != 0:
        # 1x인 경우에는 x로 표기
        if sum(array_x) != 1:
            result.append(str(sum(array_x)))
            result.append('x + ')
            result.append(str(answer_int))
        else:
            result.append('x + ')
            result.append(str(answer_int))
    elif (sum(array_x)) != 0 and answer_int == 0:
        if sum(array_x) != 1:
            result.append(str(sum(array_x)))
            result.append('x')
        else:
            result.append('x')
    else:
        result.append(str(answer_int))
    # print(result)
    return "".join(result)