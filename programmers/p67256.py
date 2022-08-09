def solution(numbers, hand):
    answer = ''
    rhand = -1
    lhand = -1
    # 각각의 숫자에서의 거리
        # 2 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, */#]
    d = { 2 : [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4],
          5 : [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3],
          8 : [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2],
          0 : [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1],
        }
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            lhand = n
        elif n in [3, 6, 9]:
            answer += 'R'
            rhand = n            
        else:
            ld = d[n][lhand] if lhand != -1 else d[n][10]
            rd = d[n][rhand] if rhand != -1 else d[n][10]

            if rd < ld or (rd == ld and hand == 'right'):
                rhand = n
                answer += 'R'
            elif rd > ld or (rd == ld and hand == 'left'):
                lhand = n
                answer += 'L'
    return answer

n = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	
h = "left"	
r = "LRLLRRLLLRR"
print(r == solution(n, h))