def solution(name, yearning, photo):    
    answer = []

    table = {n: y for n, y in zip(name, yearning)}
    for case in photo:
        score = 0
        for n in case:
            # if n in table
            try:
                score += table[n]
            except:
                continue
        answer.append(score)
        
    return answer