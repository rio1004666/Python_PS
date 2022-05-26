# 리스트 안에 있는 내부를 조작
# 투포인터 활용
from typing import List


def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right: # 같아지는 순간 반복문 빠져나온다
        s[left], s[right] = s[right], s[left] # 자리교환 바로 가능하다 임시저장소가 없어도
        left -= 1
        right -= 1
# 뒤집는것은 파이썬의 reverse()메서드가 있다
def reverseString(s: List[str]) -> None:
    s.reverse() # 리스트에만 제공되는 방식 문자열은 [::-1]이 있고 이 리스트를 문자열로 합친다음에 써도 된다.



