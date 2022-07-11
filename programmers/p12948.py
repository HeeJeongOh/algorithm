'''
SLICE
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

[ex1]
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

[ex2]
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
'''
phone_number = '023334444'

def solution1(phone_number):
    n = len(phone_number)-4
    answer = '*' * n
    for i in range(n, len(phone_number)):
        answer += phone_number[i]
    return answer

print(solution1(phone_number))

def solution2(phone_number):
    answer = '*'*(len(phone_number)-4) + phone_number[-4:]
    return answer

print(solution2(phone_number))

