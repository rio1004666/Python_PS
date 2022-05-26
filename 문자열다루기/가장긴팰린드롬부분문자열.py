"""
중앙을 중심으로 확장하는 풀이  => 투포인터 활용 풀이(슬라이딩 윈도우)
혹은 다이나믹 프로그래밍 풀이
"""


def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    if len(s) < 2 or s == s[::-1]:  # 문자열 길이가 1이거나 전체문자열을 뒤집어도 같다면 가장 긴 팰린드롬 문자열이므로 그대로 그 문자열을 반환한다.
        return s
    result = ''
    # 슬라이딩 윈도우 우측 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)  # max메서드 키값 문자열 길이로 삼겠다.
    return result
