'''
[시도1] 시간초과 2
'''
def solution(phone_book):
    phone_book.sort(key=len)
    for i, p in enumerate(phone_book):
        for phone in phone_book[i+1:]:
						# (실패 4) p in phone X
            if p == phone[:len(p)]:
                return False
    return True

'''
[시도2] 실패 2
'''
def solution(phone_book):
    nmin = len(min(phone_book))
    phone_book = [p[:nmin] for p in phone_book]
    
    if len(phone_book) == len(set(phone_book)):
        return True
    
    return False

'''
[다른사람풀이]
ㄴ 왜 (i)번째와 (i+1)만 비교하는데 통과하지 -> 문자열 sorting
["119", "97674223", "1195524421"] -> ['119', '1195524421', '97674223']
'''
def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True
