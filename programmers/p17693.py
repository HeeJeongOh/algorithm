'''
m: 네오가 기억한 멜로디
musicinfos : 곡정보를 담고 있는 배열
1. 40.0 -> return "(None)"
2. 56.7 -> getMinutes 수정
3. 
'''
import re
from datetime import datetime

def getMinutes(start, end):
    mm = 0
    st = datetime.strptime(start, '%H:%M')
    en = datetime.strptime(end, '%H:%M')
    
    mm = (en-st).seconds/60
    return int(mm)

def resub(info):
    info = re.sub('C#', 'X', info)
    info = re.sub('D#', 'Y', info)
    info = re.sub('F#', 'Z', info)
    info = re.sub('G#', 'M', info)
    info = re.sub('A#', 'N', info)
    return info

def solution(m, musicinfos):
    m = resub(m)
    print(m)
    tmp = []

    for music in musicinfos:
        start, end, title, info = music.split(',')
        # 재생시간 구하기
        mm = getMinutes(start, end)
        # '_#' 다른문자로 변경
        info = resub(info)
        # 해당 코드를 resub내에 넣을 경우, 틀리고 밖으로 꺼내면 정답 .. ?
        info = info * (mm // len(info)) + info[: mm % len(info)]
        if m in info:
            tmp.append((mm, title))

    if len(tmp) == 0:
        return "(None)"
    else:   
        # [mm, title]
        answer = tmp[0]
        for i in range(1, len(tmp)):
            # 재생시간 비교, 재생시간이 더 길 경우만 갱신
            if tmp[i][0] > answer[0]:
                answer = tmp[i]                 

    return answer[1]
    
m ="CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))
