'''
1. 시작점 (가장 높은 점 + 가장 왼쪽에 있는점)
2. 끝 점 (가장 낮은 점 + 가장 오른 쪽에 있는 점)
'''
def solution(wallpaper):
    answer = []
    xloc = []
    yloc = []
    for i, w in enumerate(wallpaper):
        for j, item in enumerate(w):
            if item == '#':
                yloc += [i]
                xloc += [j]    
    # print(xloc)
    # print(yloc)
    return [min(yloc), min(xloc), max(yloc)+1, max(xloc)+1]