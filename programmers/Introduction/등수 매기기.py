'''
영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다.
영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(score):
    # 평균 구해서 배열에 추가
    average = []
    # sum(_)//2 를 실행하면 소수점 뒷자리는 버리기 때문에 잘못된 공동 n등이 발생할 수 있음.
    for _ in score:
        average.append(sum(_)/2)
    print(average)
    
    # {평균:등수} 형태로 높은 평균 순서대로 딕셔너리에 추가
    print(sorted(average, reverse = True))
    rank = {}
    for _ in sorted(average, reverse = True):
        # 중복된 평균은 index 값이 더 앞의 것을 return 해주는 python의 성질로 해결
        rank[_] = sorted(average, reverse=True).index(_)+1
    print(rank)
    
    result = []
    for _ in range(len(average)):
        for key, value in rank.items():
            if average[_] == key:
                result.append(value)
    return result

'''
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]
'''