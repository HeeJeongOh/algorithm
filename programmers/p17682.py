def solution(dartResult):   
    answer = 0
    nums = []
    # '*'을 제외하고 미리 계산해두기
    tmp = 0
    for d in dartResult:
        if d.isnumeric():    
            if tmp == 1 and d == '0':
                tmp = 10
            else:
                tmp = int(d)
        elif d == 'S':
            tmp = tmp**1
            nums.append(tmp)
        elif d == 'D':
            tmp = tmp**2
            nums.append(tmp)
        elif d == 'T':
            tmp = tmp**3
            nums.append(tmp)
        elif d == '#':
            nums[nums.index(tmp)] = -tmp
        else:
            nums.append(d) 
        print(nums)
    
    # '*' 계산하기
    for _ in range(len(dartResult)):
        try:
            i = nums.index('*')
        except ValueError:
            answer += sum(nums)
            break
            
        if i == 1:      
            a = nums[i-1]
            nums.insert(0, a*2)            
            nums.remove(a) 
            nums.remove('*') 
        else:
            a = nums[i-1]
            b = nums[i-2]
            nums.insert(0, (a+b)*2)
            nums.remove(a)
            nums.remove(b)
            nums.remove('*') 
    return answer