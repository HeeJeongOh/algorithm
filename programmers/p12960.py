arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

def solution(arr1, arr2):
    c = len(arr1)
    r = len(arr1[0])
    answer = [[0]*r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer
print(solution(arr1, arr2))