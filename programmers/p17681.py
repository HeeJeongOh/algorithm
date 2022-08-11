def toBinary(n, arr):
    bins = []
    for a in arr:
        tmp = bin(a)[2:]
        if len(tmp) < n:
            tmp = '0'*(n-len(tmp)) + tmp
        bins.append(list(tmp))
    return bins
        
def solution1(n, arr1, arr2):
    answer = [[] for _ in range(n)]    
    map1 = toBinary(n, arr1)
    map2 = toBinary(n, arr2)
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                answer[i].append('#')
            else:
                answer[i].append(' ')
        answer[i] = "".join(answer[i])
    return answer

def solution2(n, arr1, arr2):
    ans = []
    # zip(arr1, arr2) => i, j = (arr1[idx], arr2[idx])
    for i, j in zip(arr1, arr2):
        map = str(bin(i|j)[2:])     # or, bin -> 0b____     
        map = map.rjust(n, '0')     # 왼쪽에 '0'을 넣어 길이 n 맞추기
        map = map.replace('0', ' ')
        map = map.replace('1', '#')
        ans.append(map)
    return ans

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
r = ["#####","# # #", "### #", "# ##", "#####"]

print(solution1(n, arr1, arr2))
print(solution2(n, arr1, arr2))