# find the largest 5 digits in a string of numbers

def solution(digits):
    n= 0
    for i in range(5,len(digits)+1):
        n = max(n,digits[i-5:i]) # stores the largest 5 number digit up so far
    return int(n)
