
'''
# 아마 코테에서는 불가능할 듯
import numpy as np
def solution(arr1, arr2):
    anum = np.array(arr1)
    bnum = np.array(arr2)
    return anum.dot(bnum).tolist()
[시도1]
1. arr2 열 -> 행 변경하여 계산

def solution(arr1, arr2):
    arr = []
    for i in range(len(arr2[0])):
        tmp = []
        for j in range(len(arr2)):
            tmp.append(arr2[j][i])
        arr.append(tmp)
    
    ans = []
    for a1 in arr1:
        tmp = []
        for a2 in arr:
            # print(a1, a2)
            s = 0
            for i, j in zip(a1, a2):
                s += i*j
            tmp.append(s)
        ans.append(tmp)
        
    return ans
    
[시도2] : 질문하기 참고
1. 행, 행, 행 -> 열, 열
>>> zip(*[[1,2], [3,4], [5,6]])
[(1, 3, 5), (2, 4, 6)]
-―
'''
def solution(arr1, arr2):
    ans = []
    for a in arr1:
        tmp = []
        for b in zip(*arr2):
            print(a, b)
            s = 0
            for i, j in zip(a,b):
                s += i*j
            tmp.append(s)
        ans.append(tmp)

    return ans