'''
1. 탈락 사유
    1.1 이전에 등장했던 단어
        1.1.1 단어 나올 때마다 이전에 나왔는지 비교
        1.1.2 사전에 중복되는 단어의 인덱스 찾기 - 오히려 시간 복잡도가 증가할 것으로 예상
    1.2 이전의 마지막 문자와 첫 문자가 같지 않은 경우

'''
def solution(n, words):
    answer = [0, 0]
    stack = []
    bword = ''   
    for i, w in enumerate(words):
        if w in stack or (bword != '' and bword[-1] != w[0]):
            return [(i % n)+1, (i // n)+1]
        bword = w
        stack.append(w)
        
    return answer