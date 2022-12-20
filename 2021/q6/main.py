def part1(input, num_days):
    state = [int(x) for x in input.split(',')]
    # print('Initial state:', state)
    for n in range(num_days):
        for i, s in enumerate(state):
            if s == 0:
                state.append(9)
                state[i] = 6
            else:
                state[i] -= 1

        # print(f'After {n+1} day:', state)
    return len(state)


# result = part1('3,4,3,1,2', 18)
# print('Result is:', result)
# result = part1('3,4,3,1,2', 80)
# print('Result is:', result)
# result = part1('3,4,3,1,2', 256)
# print('Result is:', result)

# input = '4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2'
# result = part1(input, 80)
# print('Result is:', result)


def part2(input, num_days):
    hist = [0] * 9
    fishes = [int(x) for x in input.split(',')]
    # print(fishes)
    for f in fishes:
        hist[f] += 1

    # print(hist)
    for n in range(num_days):
        # print(f'After {n + 1} day:', hist)
        num_zeros = hist[0]
        for h in range(8):
            hist[h] = hist[h + 1]
        # print(hist)
        hist[6] += num_zeros
        hist[8] = num_zeros
        # print(hist)
    return sum(hist)

    # # print('Initial state:', state)
    # for n in range(num_days):
    #     for i, s in enumerate(state):
    #         if s == 0:
    #             state.append(9)
    #             state[i] = 6
    #         else:
    #             state[i] -= 1
    #
    #     # print(f'After {n+1} day:', state)
    # return len(state)

result = part2('3,4,3,1,2', 256)
print('Result is:', result)

input = '4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2'
result = part2(input, 256)
print('Result is:', result)