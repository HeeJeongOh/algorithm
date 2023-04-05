def solution(s):
    letters = [int(i) for i in s.split(" ")]
    return f"{min(letters)} {max(letters)}"