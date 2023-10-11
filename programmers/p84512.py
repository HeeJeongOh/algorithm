'''
A
AA
AAA
AAAA
AAAAA
AAAAE
1. 무식하지만 유일하게 떠오르는 방식... 
'''
def solution(word):
    m = ['A', 'E', 'I', 'O', 'U']
    w = []
    for a in m:
        w += [a]
        for b in m:
            w += [a+b]    
            for c in m:
                w += [a+b+c]    
                for d in m:
                    w += [a+b+c+d]       
                    for e in m:
                        w += [a+b+c+d+e]    
        # print(w)
        if word in w:
            return w.index(word)+1
    
    return 0

'''
[다른사람풀이]
product : 데카르트 곱
'''
from itertools import product
def solution(word):
	wlist = []
	for i in range(1, 6):
		# repeat = 조합을 만들 리스트 쌍 
		# repeat = 2 : "AEIOU", "AEIOU" -> AA AE AI AO AU EA EE ...
		for c in product("AEIOU", repeat=i+1):
			wlist += ["".join(c)]
	
	wlist.sort()
	return wlist.index(word) + 1