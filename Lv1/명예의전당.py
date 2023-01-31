def solution(k, score):
    # k = 명예의 전당 랭킹 커트라인
    # score = 점수가 담긴 리스트 
    answer = []
    top_score = []
    for i in score:
        if len(top_score) == k:
            top_score.append(i)
            top_score.pop(top_score.index(min(top_score)))
            answer.append(min(top_score))
        else:
            top_score.append(i)
            answer.append(min(top_score))
    
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))