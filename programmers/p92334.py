def solution(id_list, report, k):
    answer = {id: 0 for id in id_list}
    scores = {id: [0, []] for id in id_list}

    for r in set(report):
        f, t = r.split()
        scores[t][0] += 1
        scores[t][1].append(f)

    # k번 이상 신고된 유저 : 메일 발송 
    for t in id_list:
        if scores[t][0] >= k:            
            for ff in scores[t][1]: 
                answer[ff] += 1
            
    return list(answer.values())