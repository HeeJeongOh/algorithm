def solution1(s):
    answer = ""
    dict = {'ze': ('0', 4), 'on': ('1', 3), 'tw': ('2',3), 
            'th': ('3', 5), 'fo': ('4', 4), 'fi': ('5', 4),
            'si': ('6', 3), 'se': ('7', 5), 'ei': ('8', 5),
            'ni': ('9', 4)
           }
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            answer += s[i]
            i += 1
        else:
            wrd = s[i:i+2]
            answer += dict[wrd][0]
            i = i + dict[wrd][1]
       
    return int(answer)


def solution2(s):
    num_dic = {"zero":"0", "one":"1", "two":"2", 
                "three":"3", "four":"4", "five":"5", "six":"6", 
                "seven":"7", "eight":"8", "nine":"9"}
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
    
solution1('one4seveneight')
solution2('one4seveneight')