# 정확성: 20.8 
# 합계: 20.8 / 100.0

def solution(id_list, report, k):
    answer = {id: 0 for id in id_list}

    scores = {id: [0, []] for id in id_list}
    report = list(set(report))

    for r in report:
        f, t = r.split()
        scores[t][0] += 1
        scores[t][1].append(f)
        
        if scores[t][0] == k:
            scores[t][0] = 0
            for ff in scores[t][1]: 
                answer[ff] += 1
            
    return list(answer.values())