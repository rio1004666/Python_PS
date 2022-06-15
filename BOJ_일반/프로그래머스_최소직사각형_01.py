def solution(sizes):
    # 관철 : 문제에서 요구하는 최소넓이가 되게하려면 ( 지갑가방이 )
    # w,h값 두개중 하나는 작은값들을 리스트로 큰값들 리스트로 나누어 담고 그 중 최댓값을 각각 곱합낟
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)