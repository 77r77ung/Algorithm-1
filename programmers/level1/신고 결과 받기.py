# collection
# Hash
from collections import defaultdict
def solution(id_list, report, k):
    # report에서 중복되는 값들 제거 -> {'muzi frodo', 'apeach frodo', 'apeach muzi', 'muzi neo', 'frodo neo'} 형태로 저장
    reportHash = defaultdict(set)
    countHash = defaultdict(int)
    result = []
    for i in set(report):
        a, b = i.split(" ")
        # set: 자료 수정 불가(따라서, add 문법을 사용해주어야 함)
        reportHash[a].add(b)
        countHash[b] += 1
    for name in id_list:
        mail = 0
        # reportHash[name] = value(: user)
        for user in reportHash[name]:
            # dic[key] = value
            if countHash[user] >= k:
                mail += 1
        result.append(mail)
    return result
'''
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

'''
num = 1
numbox = []
for mul in range(1, 4, 1):
    result = [_ for _ in list(map(int, str(num * mul)))]
    print(result)
    for i in result:
        if i in numbox:
            print("f")
        else:
            numbox.append(i)

print(result)
print(numbox)

x = 5
y = 2
print(x%y)