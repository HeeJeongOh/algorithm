'''
0. 문제 읽고 풀기
1. 단어의 길이 / 사전 순 정렬
2. K번째 위치한 값 내보내기
'''
def solution(K, words):
	# words.sort(key=lambda x: (len(x), x))
	words.sort()
	words.sort(key=len)
	# print(words)
	return words[K-1]
	
N, K = map(int, input().split())
words = [input() for _ in range(N)]
print(solution(K, words))