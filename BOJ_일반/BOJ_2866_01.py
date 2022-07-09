import sys

r, c = list(map(int, sys.stdin.readline().split()))

str_list = []
for i in range(r):
    str_list.append(list(map(str, sys.stdin.readline().rstrip())))

start = 0
end = len(str_list) - 1


def has_duplicate(point: int) -> bool:
    str_set = set()
    for b in range(c):  # 열
        string = ''
        for a in range(point, r):  # mid ~ 문자열 전체 끝 까지의 행
            string += str_list[a][b]
        # 중복되지 않았다면 set에 넣기
        if string not in str_set:
            str_set.add(string)
        # 중복된게 발견된 경우
        else:
            return True

    return False


answer = 0

# 어떤 동일한 문자열이 존재한다면, 그 이후의 문자열도 중복된다.
# 따라서 중복이 아직 일어나지 않는 지점을 찾아내야 한다.
while start <= end:
    mid = (start + end) // 2

    # mid ~ 문자열 끝 까지의 지점에서 중복된 문자열이 존재한다면, 중복이 더 이전에서 발생했는지 찾아 봐야 한다.
    if has_duplicate(mid):
        end = mid - 1
    # mid ~ 문자열 끝 까지의 지점에서 중복된 문자열이 없다면,
    else:
        # 중복이 아직 일어나지 않은 지점을 찾았으므로 정답 갱신
        answer = mid
        start = mid + 1

print(answer)