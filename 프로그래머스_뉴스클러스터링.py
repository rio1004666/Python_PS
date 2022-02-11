from collections import Counter

def solution(str1, str2):
    answer = 0
    # 1. 두자씩 끊어서 다중집합의 원소로 만든다
    str1_list, str2_list = [], []
    ns1, ns2 = len(str1), len(str2)
    word_set = set()
    for i in range(ns1 - 1):
        if str1[i:i + 2].isalpha():
            str1_list.append(str1[i:i + 2].lower())
            word_set.add(str1[i:i + 2].lower())
    for i in range(ns2 - 1):
        if str2[i:i + 2].isalpha():
            str2_list.append(str2[i:i + 2].lower())
            word_set.add(str2[i:i + 2].lower())
    if len(str1_list) == 0 and len(str2_list) == 0:
        return 65536
    cnt1 = Counter(str1_list)
    cnt2 = Counter(str2_list)

    intersection, union = 0, 0
    for word in word_set:
        intersection += min(cnt1[word], cnt2[word])
        union += max(cnt1[word], cnt2[word])
    if union != 0:
        answer = int(intersection / union * 65536)
    return answer

print(solution("FRANCE","french"))