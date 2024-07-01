from collections import Counter
def solution(array):
    counter = Counter(array)
    
    count = 0
    for _ in counter.most_common(): # _: (3, 3) (1, 1) (2, 1) (4, 1)
        if _[1] == counter.most_common()[0][1]: # counter.most_common()[0][1] : 최빈값
            count += 1
    return counter.most_common()[0][0] if count == 1 else -1
    