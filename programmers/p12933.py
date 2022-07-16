'''
myList = ['2022', '12', '31']
x = "-".join(myList)

>> '2022-12-31'
'''
def solution(n):
    answer = int("".join(sorted(str(n), reverse=True)))
    
    return answer

print(solution(118343))