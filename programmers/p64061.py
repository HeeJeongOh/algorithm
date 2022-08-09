def solution(board, moves):
    stack = []
    answer = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:   
            answer += 2
            stack.pop()
            stack.pop()
    return answer

b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
m = [1,5,3,5,1,2,1,4]
r = 4
print(r == solution(b, m))