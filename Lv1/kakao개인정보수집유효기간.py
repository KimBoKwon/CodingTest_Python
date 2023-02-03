def solution(today, terms, privacies):
    answer = []
    today_split_list = today.split('.')
    today = int(today_split_list[0])*12*28 + int(today_split_list[1])*28 + int(today_split_list[2])
    reterms = make_reterms(terms)

    for idx, value in enumerate(privacies):
        value_split_list = value.split(' ')
        value_split_list2 = value_split_list[0].split('.')
        day = int(value_split_list2[0])*12*28 + int(value_split_list2[1])*28 + int(value_split_list2[2])
        if day + int(reterms[value_split_list[1]]) <= today:
            answer.append(idx+1)
    return answer

def make_reterms(terms):
    reterms = {}
    for i in terms:
        split_list = i.split(' ')
        reterms[split_list[0]] = (int(split_list[1]))*28
    print(reterms)
    return reterms

    
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))