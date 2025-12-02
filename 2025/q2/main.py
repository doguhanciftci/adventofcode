import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from tools.reader import read

test_data = read('input_easy.txt')
actual_data = read('input.txt')

def isPalindrome(s):
    length = len(s)
    if(length % 2 == 1):
        return False
    return s[:length//2] == s[length//2:]

def part1(data):
    result = 0
    data = data[0]
    for item in data.split(','):
        start, end = item.split('-')
        for number in range(int(start), int(end) + 1):
            if isPalindrome(str(number)):
                result += number
        
    return result

print(f"Part 1 Test: {part1(test_data)}")
print(f"Part 1 Actual: {part1(actual_data)}")

def isInValid(s):
    length = len(s)
    if length < 2:
        return False

    def getDivisors(n):
        divisors = []
        for i in range(1, n//2 + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    def checkRepeatingN(s, n):
        for i in range(len(s) // n - 1):
            if s[i*n:(i+1)*n] != s[(i+1)*n:(i+2)*n]:
                return False
        return True

    divisors = getDivisors(length)
    for divisor in divisors:
        if checkRepeatingN(s, divisor):
            return True
    
    return False

def part2(data):
    result = 0
    data = data[0]
    for item in data.split(','):
        start, end = item.split('-')
        for number in range(int(start), int(end) + 1):
            if isInValid(str(number)):
                result += number
        
    return result

print(f"Part 2 Test: {part2(test_data)}")
print(f"Part 2 Actual: {part2(actual_data)}")