# 유효한 팰린드롬
# 문자열이 팰린드롬인지 확인하여라 => 앞뒤가 같은 문자열
# 그리고 나머지 특수기호나 이런것들은 다뺀다
# 먼저 알파벳을 소문자로 바꾸고 특문 뺀다
# 대부분 문제는 전처리가 먼저다!!!!!!!!! 제일 먼저 무엇을 해야할지 차근차근히 생각해라
def isPalindrome(s: str) -> bool:
    # 알파벳이나 숫자만 넣어준다 알파벳은 소문자로 바꿔서 넣고 특수문자는 넣지않는다
    # 단순 반복문이다.
    # 그 후 리스트메서드 앞뒤 팝을 사용햇다.
    strs = []
    for char in s:
        if char.isalnum():  # 숫자나 알파벳이면
            strs.append(char.lower())  # 소문자로 바꿔서 넣어라
    # strs = [char.lower() for char in s if char.isalnum()] 리스트 컴프리핸션 사용

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():  # 앞뒤로 하나씩 빼본다 그런데 이건 속도가 늦다
            return False
        # 데크를 사용해서 속도 더 빠르게한다.
    return True
from collections import deque
def isPalindrome2(s: str) -> bool:
    # 리스트 컴프리핸션 활용후 데크로 속도 성능 향상
    strs = [char.lower() for char in s if char.isalnum()]  # 리스트 컴프리핸션 사용
    # 특수문자 제거하고 소문자로 변경하기 위한 전처리
    queue = deque(strs)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True
print(isPalindrome2("A man, a plan, a canal: Panama"))
print(isPalindrome2("race a car"))
import re
def isPalindrome3(s:str) -> bool:
    # 정규식을 활용하여 필터링 후 슬라이싱 활용
    strs = re.sub('[^a-z0-9]','',s) # 정규 표현식으로 필터링
    return strs == strs[::-1] # 앞뒤로 같다면 리턴값은 True , 다르다면 False반환
    # 슬라이싱 사용하면 훨씬 더 성능 개선된다 그리고 내부적으로C로 구현되어 잇따.
print(isPalindrome3("A man, a plan, a canal: Panama"))
print(isPalindrome3("race a car"))