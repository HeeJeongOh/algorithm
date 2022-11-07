def solution(n,a,b):
    answer = 0
    players = [i for i in range(1,n+1)]
    players[players.index(a)] = 'a'
    players[players.index(b)] = 'b'
    while len(players) > 2:        
        answer += 1
        tmp = [(players[i:i+2]) for i in range(0,len(players),2)]
        players = []

        for j in range(len(tmp)):
            if 'a' in tmp[j]:
                if 'b' in tmp[j]:
                    return answer
                players.append('a')
            elif 'b' in tmp[j]:
                if 'a' in tmp[j]:
                    return answer
                players.append('b')
            else:
                players.append(tmp[j][0])
    return answer+1