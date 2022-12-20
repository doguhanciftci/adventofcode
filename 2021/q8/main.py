'''
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce


1 => 2:     c     f
7 => 3: a   c     f
4 => 4:   b c d   f
2 => 5: a   c d e   g
3 => 5: a   c d   f g
5 => 5: a b   d   f g
0 => 6: a b c   e f g
6 => 6: a b   d e f g
9 => 6: a b c d   f g
8 => 7: a b c d e f g




a => 1 and 7

replace c f from 2 and 3

len==2 olan 4 and 3 => common char is d
len == 1 olan 4 and 3 => replace any len==3 and find  e
len==2 olan 3 tane. 2 of them g, one of them b
'''


def analyse(input):
    map = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}
    print(input)
    original_inputs = input.strip().split(' ')
    inputs = original_inputs.copy()
    print(inputs)
    number_1 = [inp for inp in inputs if len(inp) == 2][0]
    number_7 = [inp for inp in inputs if len(inp) == 3][0]
    char_a = number_7.replace(number_1[0], '').replace(number_1[1], '')
    map['a'] = char_a
    inputs = [inp.replace(number_1[0], '').replace(number_1[1], '').replace(char_a, '') for inp in inputs if
              len(inp) > 3]

    number_4_3 = [inp for inp in inputs if len(inp) == 2]
    char_d = (set(number_4_3[0]) & set(number_4_3[1])).pop()
    map['d'] = char_d
    inputs = [inp.replace(char_d, '') for inp in inputs]
    number_4_3 = [n.replace(char_d, '') for n in number_4_3]
    number_any_length_3 = [inp for inp in inputs if len(inp) == 3][0]
    char_e = number_any_length_3.replace(char_d, '').replace(number_4_3[0], '').replace(number_4_3[1], '')
    map['e'] = char_e
    number_any_length_2 = [inp.replace(char_e, '') for inp in inputs if len(inp) == 2]
    char_g = [n for n in number_any_length_2 if len(n) == 1][0]
    map['g'] = char_g
    char_b = [n for n in number_any_length_2 if len(n) == 2][0].replace(char_g, '')
    map['b'] = char_b
    f_count = len([i for i in original_inputs if number_1[0] in i])
    if f_count == 9:
        map['f'] = number_1[0]
        map['c'] = number_1[1]
    else:
        map['f'] = number_1[1]
        map['c'] = number_1[0]
    return {v: k for k, v in map.items()}


def decodeWithMap(str, map):
    result = ''
    for s in str:
        result += map[s]
    if len(result) == 2:
        return 1
    elif len(result) == 3:
        return 7
    elif len(result) == 4:
        return 4
    elif len(result) == 7:
        return 8
    elif len(result) == 5:
        if 'b' in result:
            return 5
        elif 'e' in result:
            return 2
        else:
            return 3
    elif len(result) == 6:
        if 'c' not in result:
            return 6
        elif 'e' in result:
            return 0
        else:
            return 9
    else:
        return 0


def part1(filename):
    print(filename)
    file = open(filename, 'r')
    lines = [line.strip().split('|') for line in file.readlines()]
    count = 0
    sum = 0
    for line in lines:
        map = analyse(line[0])
        output = line[1].strip().split(' ')
        # print(output)
        number = ''
        for o in output:
            decoded = decodeWithMap(o, map)
            if decoded in [1, 4, 7, 8]:
                count += 1
            number += str(decoded)
        print(number)
        sum += int(number)
        # print(map)
    print(count)
    print(sum)


part1('input_easy.txt')
part1('input.txt')
