"""
  이베이 코리아 난이도 2시간 100점맞기 가장 어려움... 역대급이다.

  1. 100점 맞기에 가장 어려웠음 ( 시간 + 난이도 고려 )
  2. 벡엔드 문제
  3. 류호석님은 1 , 2 , 4 , 5번에 50분 정도 씀
  4. 3번에 1시간 10분을 썻으나 시간초과 당함
  5. 코테를 수십번 보았는데 처음으로 만점이 아님.....
  6. 카카오 블라인드 2시간 만점 ... 이건 안됨
   1번 3번을 파이썬으로 풀엇고 나머지 c++로 풀엇지만
   3번에서 시간초과나서 다시 c++로 풀엇다. => 다시 시간초과
   특히 5번은 역대급으로.....

    1번 문제 => 테크닉 문제

   날짜와 시간 = 완전탐색 총 경우의수가 1024가지 전부 매칭
   가능한 배치인지 확인만 해주면 된다.
   문자열이 난무하는 문제는 파이썬으로 푸는것이 좋다
   날짜와 시분까지만
   날짜를 시간으로(가장작은단위로) 변경하는 것을 먼저함
   여기서는 분으로 변경 목요일 4시 30분 이면 이것을 분으로 바꿈
   비교를 해야하므로 일단 바꾼다
   숫자로 다루는 것이 편하다
   월요일  MON 은 0으로 바꾸고
          TU는 1로 바꾸고
    이제 완전탐색하면서 DFS로 IDX번 과목이 가능한 시간대가 J이면
    J시간에 들을것
    K시간에 이미 다른과목 들음
    겹치면 실패
    안겹치면 재귀호출
    한과목에 90분 수업
    A라는 과목과 B라는 과목이 겹치는지
    두 구간중 겹치는 부분이 있는지 판단
    어떻게?? 첫번재 수업이 L1부터 R1이고
    두번째 수업리 L2부터 R2까지이면
    MAX(L1,L2) < MIN(R1,R2) 로 판단 <-  이부분이 핵심 아이디어다 여기서 어떤 시간이든 구애받지 않기에
    그러면 둘중 나중에 시작하는 시간과 끝나는 시간중에 빨리 끝나는
    시간이 크다면 겹친다고 판단

    복잡도는 4 X 4 X 4 X 4 X 4  총 1024개 ** 완탐은 이렇게 시간복잡도가 크지 않다

    <<<  내 생각  >>>

    카카오와 비슷한문제긴함....2018년도 추석트래픽문제와 비슷.....

"""
n, m = 5, 4
ans = 0
selected = []
day_map = {'MO': 0, 'TU': 1, 'WE': 2, 'TH': 3, 'FR': 4}
# 문자열(요일) 숫자로 매핑해주는 맵자료구조 사용

def conv(tz):
     # 이렇게 시간으로 변환하는 기능을 함수화한다.
    # 보통 날짜 시간문제는 최소단위 시간으로 바꿔서 비교한다.
    # 요일도 시간도 분도 2개씩 들어오므로 파이썬에서는 쉽게 파싱 가능 하다
    return day_map[tz[:2]] * 60 * 24 + int(tz[3:5]) * 60 + int(tz[6:8])


def parse(tz):
    # 이렇게 파싱하는 기능을 함수화한다.
    if len(tz) == 8: # 1 과목을 듣는 경우 (3시간)
        v = conv(tz)
        return [(v, v + 90), (v + 90, v + 180)]
        # 규칙성을 깨지 않게 하기 위해  L1 R1 / L2 R2 로 바꾸기 위해서 나누었지만
        # 머 이럴필요는 없다 그런데 이러한 생각이 필요하긴 하다
    else: # 2 과목을 듣는 경우 (1시간 30분 /  1시간 30분)
        v1 = conv(tz[:8])
        v2 = conv(tz[9:])
        return [(v1, v1 + 90), (v2, v2 + 90)]


def conflict(A, B):  # A, B는 모두 시간 (요일 + 시간 + 분) 이 부분이 핵심이다 겹치는지 확인하는 부분
    A = parse(A)
    B = parse(B)
    for a in A:
        for b in B:
            if max(a[0], b[0]) < min(a[1], b[1]):
                return True
    return False


def dfs(idx, schedule): # dfs완탐은 류호석님 깃허브 참고
    if idx == len(schedule): # 첫과목선탣 -> 첫과목선택 -> 첫과목선택 .... 끝까지 탐색후에 리턴 1
        print(selected)
        return 1
    ret = 0
    for j in schedule[idx]:  # j 시간에 들을 것
        flag = True # 겹쳤는지 안겹쳤는지 확인하는 플래그 변수
        for k in selected:  # k 시간에 이미 다른 과목 들음
            if conflict(j, k):  # 겹치면 실패( 다음 과목 겹치는지 확인 ㄱㄱ)
                flag = False # 예시에서 마지막 과목들은 전부 금요일 15시로 겹치므로 false
        if flag:  # 안 겹치면 재귀호출
            selected.append(j) # 안겹친 과목 selected 리스트에 추가
            ret += dfs(idx + 1, schedule) # 각각에 대해 똑 각각 결과값을 더한다. 누적
            selected.pop()
    # 마지막 선택할 과목들을의 경우의수의 답들을 모두 모아서
    # 마지막 전에 선택할 과목들로 합산하여 결과를 리턴한다
    print(ret)
    return ret


def solution(schedule):
    return dfs(0, schedule)

print(solution([["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]))
