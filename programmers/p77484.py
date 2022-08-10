def solution(lottos, win_nums):    
    rank = [6, 6, 5, 4, 3, 2, 1]
    min = 0
    for l in lottos:
        if l in win_nums:
            min += 1
    max = min + lottos.count(0)    
    return [rank[max], rank[min]]

l = [44, 1, 0, 0, 31, 25]	
w = [31, 10, 45, 1, 6, 19]	
r = [3, 5]

print(solution(l, w))