'''
전위순회 결과 -> 후위순회
1. 입력
    1.1 숫자가 아닌 값 입력 시 while문 종료를 통해 강제종료 생성
2. 재귀함수 작성
    2.1 
'''

import sys
sys.getrecursionlimit()

tree = []
while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        tree.append(n)
    except:
        break

def postorder(first, end):
    if first > end:
        return

    mid = end+1   # 루트보다 큰 값이 존재하지 않을 경우 대비  

    # 루트보다 큰값 찾아 서브트리로 나누기
    for i in range(first+1, end+1):
        if tree[first] < tree[i]:
            mid = i
            break
    
    postorder(first+1, mid-1)
    postorder(mid, end)
    print(tree[first])

# 배열 인덱스는 0부터 시작
postorder(0, len(tree)-1)