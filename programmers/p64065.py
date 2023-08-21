def solution(s):     
    s = s[1:-1].split("},{")
    for idx, item in enumerate(s):
        s[idx] = item.replace("{", "").replace("}", "")
    s.sort(key=len)
    # print(s)
    
    answer = []
    for item in s:
        for i in item.split(","):
            if int(i) not in answer:
                answer += [int(i)]
                
    return answer