'''
1. 모든 정보가 다 담겨있는 리스트 생성
2. 재생횟수로 정렬한 후 순서대로 딕셔너리에 삽입
    2.1 각 장르를 재생횟수 합으로 정렬 
        ㄴ 처음에 문제를 잘못 읽고 그냥 재생횟수로 정렬 후 처음으로 나타나는 순서로 grank 생성
    2.2 재생횟수 순서로 곡 정렬
3. 각 장르의 최다 재생곡 2곡 추출

(+) enumerate와 zip 같이 쓸 땐 idx, (g, p) 괄호 필요
(+) tmp에 모든 정보를 담는 방식 대신 구조체를 사용한 경우도 존재
'''
from collections import defaultdict
def solution(genres, plays):

    ### 1
    gdict = defaultdict(int)
    tmp = []
    for idx, (g, p ) in enumerate(zip(genres, plays)):
        gdict[g] += p
        tmp.append([idx, g, p])
    
    ### 2
    # 2.1 장르 정렬
    grank = sorted(gdict, key=gdict.get, reverse=True)
    # 2.2 곡 정렬
    tmp = sorted(tmp, key=lambda x:x[2], reverse=True)
    # 위를 합치어 하나의 딕셔너리에 담음 
    dd = {i: [] for i in range(len(grank))}
    for t in tmp:
        dd[grank.index(t[1])].append([t[0], t[2]])
    # print(dd)
    
    ### 3
    ans = []
    for key in dd:
        for idx, _ in dd[key][:2]:
            ans += [idx]
    
    return ans