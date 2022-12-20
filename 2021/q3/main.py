def part1(filename):
    file = open(filename, 'r')
    lines = [line.strip() for line in file.readlines()]
    print(lines)
    total = len(lines)
    hist = [0] * len(lines[0])
    for line in lines:  # 00100
        for i, l in enumerate(line):
            hist[i] += int(l)
    print(hist)
    gama = [1 if h > total / 2 else 0 for h in hist]
    gamaBinary = BinaryToDecimal(gama)

    epsilon = [1 if h < total / 2 else 0 for h in hist]
    epsilonBinary = BinaryToDecimal(epsilon)
    return gamaBinary * epsilonBinary


def BinaryToDecimal(arr):
    total = 0
    for i, v in enumerate(arr):
        total += int(v) * 2 ** (len(arr) - i - 1)
    return total


#
# result = part1('input.txt')
# print(result)


def part2(filename, flag):
    file = open(filename, 'r')
    lines = [line.strip() for line in file.readlines()]
    print(lines)
    bit_length = len(lines[0])
    print(f'bit_lenght: {bit_length}')
    for bit in range(bit_length):
        ones, zeros = [], []
        for l in lines:
            if l[bit] == '0':
                zeros.append(l)
            else:
                ones.append(l)
        if flag:
            if len(ones) >= len(zeros):
                lines = ones
            else:
                lines = zeros
        else:
            if len(zeros) <= len(ones):
                lines = zeros
            else:
                lines = ones
        if len(lines) == 1:
            break
        print(lines)
    print(lines)
    return BinaryToDecimal(lines[0])


result1 = part2('input_easy.txt', True)
result2 = part2('input_easy.txt', False)
print(result1, result2, result1 * result2)


result1 = part2('input.txt', True)
result2 = part2('input.txt', False)
print(result1, result2, result1 * result2)