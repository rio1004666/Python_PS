
# C와 C#은 다르다
# C#은 1분으로 간주한다
# 그러므로 C#을 다른것으로 대체한다

def changecode(musiccode):
    # 계속 연쇄적으로 적용가능하다 ( 문자열의 강력한 라이브러리 )
    musiccode = musiccode.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    return musiccode

# 시간을 분으로 바꾼후에 인덱스와 함께 저장

# 그냥 파싱해서 60곱하고 더해도 되고 , 나눗셈과 나머지연산으로 시간을 구해도 된다


def change_minute(start, end):
    # split를 사용하면 리스트로 반환된다 그리고 리스트끼리 합쳐서 새로운 리스트가 탄생할 수 있다

    # map함수로 모두 정수형으로 일괄 적용할 수 있다

    # start_hour,start_min,end_hour,end_min = map(int, start.split(':') + end.split(':'))

    start_hour, start_min = start[:2], start[3:]

    end_hour, end_min = end[:2], end[3:]

    total_time = (int(end_hour) - int(start_hour)) * 60 + int(end_min) - int(start_min)

    return total_time


def solution(m, musicinfos):
    answer = []
    m = changecode(m)  # 악보뿐만 아니라 기억하고 있는 음들도 같이 바꿔줘야한다
    for idx, musicinfo in enumerate(musicinfos):

        musicinfo = changecode(musicinfo)

        musicinfo = musicinfo.split(',')

        time = change_minute(musicinfo[0], musicinfo[1])

        # 재생시간을 반환함
        # 이제 재생시간만큼 악보가 반복되는 것을 반환할 차례임
        # 일일이 while문을 돌리지말고 나눗셈연산과 나머지연산을 사용함
        # 위에서 이미 #코드를 다 치환했으므로 이렇게 갯수를 구한는것으로 끝이 난다

        n = len(musicinfo[3])

        melody = ''

        if n >= time:
            # 재생시간보다 악보가짧게 끝난다면 악보길이만큼만 재생하고 끝이 난다
            melody = musicinfo[3][:time]

        else:
            # 재생시간보다 악보가 계속 이어진다면

            mok = time // n
            nam = time % n

            melody = musicinfo[3] * mok + musicinfo[3][:nam]  # 파이썬의 문자열 강력한 기능

        if m in melody:
            answer.append([time, idx, musicinfo[2]])

        # 밑의 코드와 같이 바로 그냥 답을 갱신해주는 것이 좋다

        # 맨처음 등장하는것이라면 바로 넣어주고 그다음부터는 재생시간이 크냐 그다음 재생시간 같다면 더 빨리 재생된것이라면

        # if answer == None or answer[0] < duration or (answer[0] == duration and answer[1] > start):
        # answer = (duration, start, title)

    if len(answer) != 0:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))

        return answer[0][2]

    return "(None)"