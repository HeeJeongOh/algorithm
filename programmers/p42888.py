'''
- 이름과 닉네임에 대한 db 생성
- 출력 시 db참고하여 반환
'''
def solution(record):
    case = {}
    for s in record:
        tmp = s.split()
        if tmp[0] == 'Enter' or tmp[0] == 'Change':
            case[tmp[1]] = tmp[2]
    
    answer = []
    for s in record:
        result = ''
        tmp = s.split()
        if tmp[0] == 'Enter':
            result += case[tmp[1]] + '님이 들어왔습니다.'
        elif tmp[0] == 'Leave':
            result += case[tmp[1]] + '님이 나갔습니다.'
        else:
            continue
        answer.append(result)
        
    return answer

r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(r))