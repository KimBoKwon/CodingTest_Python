# def solution(k, m, score):
#     answer = 0
#     if 3 <= k <= 9 and 3 <= m <= 10 and 7 <= len(score) <= 1000000:
#         while True:
#             result_arr = []
#             if (len(score) < m):
#                 break
#             else:
#                 for i in range(m):
#                     result_arr.append(max(score))
#                     score.pop(score.index(max(score)))
#                 result = min(result_arr) * m
#                 answer += result
#         return answer
#     else:
#         return answer


# 파이썬 풀이
def solution(k, m, score):
    answer = 0 
    score = sorted(score, reverse = True)
    print(score)
    
    for i in range(0, len(score), m):
        print('i', i)
        tmp = score[i:i+m]
        print(tmp)
        
        if len(tmp) == m:
            answer += min(tmp) * m
        
    return answer

# print(solution(3, 4, [7, 7, 7, 7, 7, 7, 7]))
# print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
# print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))