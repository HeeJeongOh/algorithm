''' https://mgyo.tistory.com/185
hanoi(n, frm, to, sub) : (n-1)개의 원반을 frm에서 to로 이동하기
- frm에서 (n-1)번째까지는 sub으로, n번째는 to으로
- frm에서 (n-1)번째까지는 to로
hanoi(2, 1, 2, 3) - [frm, sub] [frm, to] [sub, to]
hanoi(3, 1, 2, 3) - hanoi(2, frm, to, sub) + [frm, to]
'''

def move(frm, to, mid, n, answer):
    if n == 1:
        answer.append([frm, to])
        return
    # 1~(n-1)번째 원반 : 1->3->2
    move(frm, mid, to, n - 1, answer)
    # n번째 원반 : 1->3
    answer.append([frm, to])
    # 1~(n-1)번째 원반 : 2->3
    move(mid, to, frm, n - 1, answer)

def solution(n):
    answer = []
    move(1, 3, 2, n, answer)
    return answer