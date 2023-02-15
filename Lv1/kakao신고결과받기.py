def solution(id_list, report, k):
    declaration = make_id_list(id_list)
    report_dic = make_report(report, id_list)
    stop_user = []
    answer = []
    for i in range(len(report_dic)):
        if id_list[i] in report_dic:
            for j in report_dic[id_list[i]]:
                declaration[j] += 1
    
    for i in range(len(declaration)):
        if declaration[id_list[i]] >= k:
            stop_user.append(id_list[i])
    
    for i in range(len(id_list)):
        cnt = 0
        if id_list[i] in report_dic:
            for j in stop_user:
                if j in report_dic[id_list[i]]:
                    cnt += 1
        answer.append(cnt)

    return answer

def make_report(report, id_list):
    report_dic = {}
    for i in range(len(report)):
        report_list = report[i].split(" ")
        if report_list[0] != report_list[1]:
            if report_list[0] in report_dic:
                if report_list[1] not in report_dic[report_list[0]]:
                    report_dic[report_list[0]] = report_dic[report_list[0]] + " " + report_list[1]
            else:
                report_dic[report_list[0]] = report_list[1]

    for j in id_list:
        if j in report_dic:
            if " " in report_dic[j]:
                report_dic[j] = report_dic[j].split(" ")
            else:
                report_dic[j] = [report_dic[j]]

    return report_dic

def make_id_list(id_list):
    declaration = {}
    for i in range(len(id_list)):
        declaration[id_list[i]] = 0

    return declaration

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo", "muzi frodo", "muzi muzi", "frodo neo","muzi neo","apeach muzi"], 2))

# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))