open_close = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}
close_scores = {
    ')': 3,
    '}': 1197,
    ']': 57,
    '>': 25137
}

open_scores = {
    ')': 1,
    '}': 3,
    ']': 2,
    '>': 4
}


def part1(filename):
    file = open(filename, 'r')
    lines = [line.strip() for line in file.readlines()]
    score = 0
    for line in lines:
        # print('\n', line)
        stack = []
        for l in line:
            if l in open_close.keys():
                stack.append(l)
            else:
                popped = stack.pop()
                if l == open_close[popped]:
                    continue
                else:
                    # print(l, popped)
                    score += close_scores[l]
    return score


#
# result = part1('ex1.txt')
# print('result is', result)
#
# result = part1('input.txt')
# print('result is', result)
#

def part2(filename):
    file = open(filename, 'r')
    lines = [line.strip() for line in file.readlines()]
    scores = []
    for line in lines:
        stack = []
        correct = True
        for l in line:
            if l in open_close.keys():
                stack.append(l)
            else:
                popped = stack.pop()
                if l == open_close[popped]:
                    continue
                else:
                    correct = False
        if correct and len(stack) != 0:
            print(line)
            print(stack)
            score = 0
            for i in range(len(stack)):
                popped = stack.pop()
                score = score * 5 + open_scores[open_close[popped]]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


result = part2('input_easy.txt')
print('result is', result)
#
result = part2('input.txt')
print('result is', result)
