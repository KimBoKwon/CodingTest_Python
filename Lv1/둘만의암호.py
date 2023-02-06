def solution(s, skip, index):
    answer = ''
    english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s_list = []
    s_list2 = []
    skip_list = []
    for i in range(len(s)):
        s_list.append(s[i])
    for i in range(len(skip)):
        skip_list.append(skip[i])
    for i in s_list:
        middle_list = []
        idx = english.index(i)
        # print(idx)
        for j in range(idx+1, idx+index+1):
            middle_list.append(english[j])
        num = idx+index+1
        num2 = 0
        for z in range(len(middle_list)):
            if middle_list[z] in skip_list:
                middle_list.pop(z)
                try:
                    middle_list.append(english[num])
                    num = num + 1
                except:
                    middle_list.append(english[num2])
                    num = num + 1
                    num2 = num2 + 1
        s_list2.append(middle_list[index-1])
    for i in s_list2:
        answer += i
    return answer

print(solution("ybcde", "az", 1))