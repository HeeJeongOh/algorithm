# 런타임에러 - O(n!)
#  def solution(s):
#     if len(s) % 2 != 0:
#         return 0
    
#     for i in range(len(s)):   
#         print(s)
#         if s[i] == s[i+1]:
#             s = s[:i] + s[i+2:]
#             i = 0
#             if len(s) == 2 and s[0] == s[1]:
#                 return 1
#     return 0

# O(n)
def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)): 
        if len(stack) != 0 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
            
    if len(stack) == 0:
        return 1       
    
    return 0

print(solution('baabaa'))
print(solution('cdcd'))