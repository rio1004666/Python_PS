1.
def solution(region, num, info):
    arr = []
    for idx, x in enumerate(info):
        r = 0
        if x[0] == region:
            r = 0
        else:
            r = 1
        arr.append((r, -(x[1] * 2 + x[2] + x[3] * 5 + 9), idx))
    arr.sort()
    answer = [-1 for _ in range(len(info))]
    for idx, x in enumerate(arr[:num]):
        answer[x[2]] = idx + 1
    return answer
