from collections import defaultdict

def solution(id_list, report,k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)
	
    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a,b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1

    print(user)
    
    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u]>=k:
                result +=1
        answer.append(result)
    return answer

# def solution(id_list, report, k):
#     declaration = make_id_list(id_list)
#     report_dic = make_report(report, id_list)
#     stop_user = []
#     answer = []
#     for i in range(len(report_dic)):
#         if id_list[i] in report_dic:
#             for j in report_dic[id_list[i]]:
#                 declaration[j] += 1
    
#     for i in range(len(declaration)):
#         if declaration[id_list[i]] >= k:
#             stop_user.append(id_list[i])
    
#     for i in range(len(id_list)):
#         cnt = 0
#         if id_list[i] in report_dic:
#             for j in stop_user:
#                 if j in report_dic[id_list[i]]:
#                     cnt += 1
#         answer.append(cnt)

#     return answer

# def make_report(report, id_list):
#     report_dic = {}
#     for i in range(len(report)):
#         report_list = report[i].split(" ")
#         if report_list[0] != report_list[1]:
#             if report_list[0] in report_dic:
#                 if report_list[1] not in report_dic[report_list[0]]:
#                     report_dic[report_list[0]] = report_dic[report_list[0]] + " " + report_list[1]
#             else:
#                 report_dic[report_list[0]] = report_list[1]

#     for j in id_list:
#         if j in report_dic:
#             if " " in report_dic[j]:
#                 report_dic[j] = report_dic[j].split(" ")
#             else:
#                 report_dic[j] = [report_dic[j]]

#     return report_dic

# def make_id_list(id_list):
#     declaration = {}
#     for i in range(len(id_list)):
#         declaration[id_list[i]] = 0

#     return declaration

# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo", "muzi frodo", "muzi muzi", "frodo neo","muzi neo","apeach muzi"], 2))

# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
