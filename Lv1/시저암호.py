def solution(s, n):
    answer = ''
    small_english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    big_english = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    new_s = list(s)
    for i in range(len(new_s)):
        if new_s[i] in small_english:
            index = small_english.index(new_s[i])
            try:
                new_s[i] = small_english[index+n]
            except:
                e_index = (index + n) - len(small_english)
                new_s[i] = small_english[e_index]
        elif new_s[i] in big_english:
            index = big_english.index(new_s[i])
            try:
                new_s[i] = big_english[index+n]
            except:
                e_index = (index + n) - len(big_english)
                new_s[i] = big_english[e_index]
    answer = listToString(new_s)
    return answer

def listToString(str_list):
    result = ""
    for s in str_list:
        result += s
    return result.strip()

print(solution("a B z",26))