def solution(new_id):        
    ans = ''

    # 1단계
    a = new_id.lower()

    # 2, 3단계
    for i in range(len(a)):
        if len(ans) > 0 and ans[-1] == '.' and a[i] == '.':
            continue
        if a[i].isalpha() or a[i].isdigit() or a[i] in  ['-', '_', '.']:
            ans += a[i]

    # 4단계
    if ans[0] == '.':
        ans = ans[1:]
    if len(ans) > 1 and ans[-1] == '.':
        ans = ans[:-1]
        

    # 5단계
    if len(ans) == 0:
        ans += 'a'
        
    # 6, 7단계   
    if len(ans) < 3:
        ans += (ans[-1]*3)
        ans = ans[:3]        
    elif len(ans) > 15:
        ans = ans[:15] 
        if ans[-1] == '.':
            ans = ans[:-1]
    
    return ans

id = "=.="	
r = "aaa"

print(r==solution(id))