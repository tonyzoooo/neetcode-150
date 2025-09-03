from utils.utils import timeit

@timeit
def is_anagram(s:str, t:str) -> bool:
    if (len(s)!=len(t)): return False
    s = sorted(s)
    t = sorted(t)
    return s == t

@timeit
def is_anagram_v2(s:str, t:str) -> bool:
    if (len(s)!=len(t)): return False
    letters = [0] * 26
    for i in range(len(s)):
        letters[ord(s[i]) - ord('a')] += 1
        letters[ord(t[i]) - ord('a')] -= 1
    for count in letters:
        if count != 0: return False
    return True