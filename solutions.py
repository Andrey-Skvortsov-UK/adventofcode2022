from copy import copy
from typing import List, Union
from collections import defaultdict
from operator import itemgetter
import sys

solutions = sys.modules[__name__]


def data(day: int, as_str: bool = False) -> Union[str, List[str]]:
    result = open(f'day#{day}.txt').read()
    if not as_str:
        result = result.splitlines()
    return result


def day_1():
    return (
        max(
            map(
                eval,
                data(1, True)
                .replace('\n\n', ',')
                .replace('\n', '+')
                .split(',')
            )
        ),
        sum(
            sorted(
                map(eval,
                    data(1, True)
                    .strip('\n')
                    .replace('\n\n',',')
                    .replace('\n', '+')
                    .split(',')
                    )
            )[-3:]
        )
    )


def day_2():
    return (
        sum(
            map(
                {
                    'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3 + 0,
                    'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
                    'C X': 1 + 6, 'C Y': 2 + 0, 'C Z': 3 + 3,
                }.setdefault,
                data(2),
            )
        ),
        sum(
            map(
                {
                    'A X': 3 + 0, 'B X': 1 + 0, 'C X': 2 + 0,
                    'A Y': 1 + 3, 'B Y': 2 + 3, 'C Y': 3 + 3,
                    'A Z': 2 + 6, 'B Z': 3 + 6, 'C Z': 1 + 6,
                }.setdefault,
                data(2)
            )
        )
    )


def day_3():
    part_1 = sum(
        ord(l) - int(l.upper() == l) * 38 - int(l.lower() == l) * 96
        for l in
        [
            list(set(s[:len(s) // 2]).intersection(s[len(s) // 2:]))[0]
            for s in data(3)
        ]
    )

    rucksacks = list(map(set, data(3)))
    groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
    badges = [list(set.intersection(*group))[0] for group in groups]
    part_2 = sum(
        ord(l) - int(l.upper() == l) * 38 - int(l.lower() == l) * 96
        for l in badges
    )

    return part_1, part_2


def day_4():
    sections = [
        list(map(int, (a, b, c, d)))
        for (a, b), (c, d) in [
            (a.split('-'), b.split('-'))
            for a, b in [line.split(',') for line in data(4)]
        ]
    ]
    return(
        sum(
            int((a >= c and b <= d) or (a <= c and b >= d))
            for a, b, c, d in sections
        ),
        sum(
            int(c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b)
            for a, b, c, d in sections
        )
    )


def day_5():
    stacks = defaultdict(str)
    data_in = data(5)

    for line in data_in[:8]:
        for index, i in enumerate(range(1, 4 * 9, 4), 1):
            stacks[index] += line[i].strip()

    stacks_2 = copy(stacks)

    moves = [line.split(' ') for line in data_in[10:]]

    for _, cnt, _, x, _, y in moves:
        cnt, x, y = map(int, [cnt, x, y])
        stacks[y] = stacks[x][:cnt][::-1] + stacks[y]
        stacks[x] = stacks[x][cnt:]
        stacks_2[y] = stacks_2[x][:cnt] + stacks_2[y]
        stacks_2[x] = stacks_2[x][cnt:]

    return(
        ''.join(map(itemgetter(0), stacks.values())),
        ''.join(map(itemgetter(0), stacks_2.values()))
    )


def day_6():
    data_in = data(6, True)
    i = 4
    while len(set(data_in[i - 4:i])) < 4:
        i += 1
    j = 14
    while len(set(data_in[j - 14:j])) < 14:
        j += 1
    return i, j


def day_7():
    data_in = data(7)
    path = []
    dirs = defaultdict(int)

    def add_size(path: List[str], size: int):
        for i in range(len(path)):
            dirs[tuple(path[:i + 1])] += size

    for line in data_in:
        if line.startswith('$ cd ..'):
            path.pop()
        elif line.startswith('$ cd /'):
            path = ['/']
        elif line.startswith('$ cd'):
            path.append(line[4:].strip())
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            continue
        else:
            size, _ = line.split(' ')
            add_size(path, int(size))

    result_1 = sum(value for value in dirs.values() if value <= 100000)

    total_size = dirs[('/',)]
    delta = total_size - 40000000
    candidates = {key: v for key, v in dirs.items() if v >= delta}
    sorted_candidates = sorted(candidates.items(), key=lambda item: item[1])
    return result_1, sorted_candidates[0][1]


def day_8():
    data_in = data(8)
    x = len(data_in[0])
    y = len(data_in)

    cnt = 0
    for i in range(1, x - 1):
        for j in range(1, y - 1):
            cnt += int(any(
                [
                    all(data_in[j][i] > data_in[j][k] for k in range(i + 1, x)),
                    all(data_in[j][i] > data_in[j][k] for k in range(0, i)),
                    all(data_in[j][i] > data_in[k][i] for k in range(j + 1, y)),
                    all(data_in[j][i] > data_in[k][i] for k in range(0, j)),
                ]
            ))
    result_1 = 2 * (x + y) - 4 + cnt

    max_score = 0
    for i in range(1, x - 1):
        for j in range(1, y - 1):
            z1, z2, z3, z4 = 0, 0, 0, 0
            for k in range(i + 1, x):
                z1 += 1
                if data_in[j][i] <= data_in[j][k]:
                    break
            for k in range(i, 0, -1):
                z2 += 1
                if data_in[j][i] <= data_in[j][k - 1]:
                    break
            for k in range(j + 1, y):
                z3 += 1
                if data_in[j][i] <= data_in[k][i]:
                    break
            for k in range(j, 0, -1):
                z4 += 1
                if data_in[j][i] <= data_in[k - 1][i]:
                    break
            score = z1 * z2 * z3 * z4
            if score > max_score:
                max_score = score

    return result_1, max_score


if __name__ == '__main__':
    for f in dir():
        if f.startswith('day'):
            print(f'{f}:', getattr(solutions, f)())
