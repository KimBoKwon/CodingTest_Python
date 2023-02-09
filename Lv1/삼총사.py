# def solution(number):
#     answer = 0
#     for i in range(len(number)):
#         first_num = number[i]
#         for j in range(i+1, len(number)):
#             second_num = number[j]
#             for z in range(j+1, len(number)):
#                 if(first_num + second_num + number[z] == 0):
#                     answer += 1
#     return answer


from itertools import combinations

def solution(number) :
    answer = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            answer += 1
    return answer

# (-2, 3, 0)
# (-2, 3, 2)
# (-2, 3, -5)
# (-2, 0, 2)
# (-2, 0, -5)
# (-2, 2, -5)
# (3, 0, 2)
# (3, 0, -5)
# (3, 2, -5)
# (0, 2, -5)

print(solution([-2, 3, 0, 2, -5]))