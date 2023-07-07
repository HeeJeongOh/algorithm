'''
[시도1] 0.0 / 100.0
1. 수직선을 그린다고 생각하여 영역 갯수 세기
    1.1 범위 내에 있는 숫자를 기억하기
    1.2 경계값만 기억하기
    1.3 예외처리 
def solution(routes):

    routes.sort()
    print(routes)
    cam = [routes.pop(0)[1]]

    for i, o in routes:
        # 다음 경로에 이미 카메라가 포함되어 있지 않은 경우
        if cam[-1] not in range(i, o):
						# 예외처리
            if cam[-1] > i:
                cam.pop()
                cam += [i]
            else:
                cam += [o]
    print(cam)
    return len(cam)
----------------------------
[시도2]
1. cam이 될 수 있는 경우의 수 늘리기
    1.1 [-100, 100], [50, 170] -> cam = 50이 될 수 있게
    1.2 [[0, 1], [0, 1], [1, 2]] -> cam = 1 하나
def solution(routes):
		# 2차원 문자열 중복제거를 위해 튜플로 변경
		routes = sorted(list(set(list(map(tuple, routes)))))    # print(routes)
    cam = [routes[0][1]]
    for idx, (rin, rout) in enumerate(routes[1:]):
        # print(cam)
        c = cam[-1]
        # print(c, rin, rout, routes[idx-1])
        if c in range(rin, rout) or rin in range(routes[idx][0], routes[idx][1]):
            if c > rin:
                # print('rin')
                cam.pop()
                cam.append(rin)
        else:
            # print('c, rout')
            cam.append(rout)
    return len(cam)

[시도3] 질문하기 참고
1. routes 정렬을 진출시점, 진입시점으로 설정
	ㄴ 왱 ...?
'''
def solution(routes):
    # 2차원 문자열 중복제거를 위해 튜플로 변경
    routes.sort(key=lambda x:(x[1], x[0]))
    # print(routes)
    cam = [routes[0][1]]
    
    for idx, (rin, rout) in enumerate(routes[1:]):
        # print(cam[-1], (rin, rout))
        if cam[-1] not in range(rin, rout):
            cam.append(rout)
            
    # print(cam)
        
    return len(set(cam))