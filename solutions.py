from copy import copy, deepcopy
from dataclasses import dataclass
from functools import cmp_to_key
from itertools import zip_longest, chain
from typing import List, Union, Dict, Optional
from collections import defaultdict
from operator import itemgetter
import sys

solutions = sys.modules[__name__]


def data(day: int, as_str: bool = False) -> Union[str, List[str]]:
    result = open(f'day#{day}.txt').read()
    if not as_str:
        result = result.splitlines()
    return result


def day_01():
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


def day_02():
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


def day_03():
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


def day_04():
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


def day_05():
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


def day_06():
    data_in = data(6, True)
    i = 4
    while len(set(data_in[i - 4:i])) < 4:
        i += 1
    j = 14
    while len(set(data_in[j - 14:j])) < 14:
        j += 1
    return i, j


def day_07():
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


def day_08():
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


def day_09():
    data_in = data(9)
    moves = list(map(lambda x: x.split(' '), data_in))

    def print_robe(robe, f, knots):
        f.write('\n\n')
        X = [knot[0] for knot in robe]
        Y = [knot[1] for knot in robe]
        x0, x1 = min(X), max(X)
        y0, y1 = min(Y), max(Y)

        lx = x1 - x0 + 2
        ly = y1 - y0 + 2
        grid = [['.' for _ in range(lx)] for __ in range(ly)]
        for i in range(knots):
            grid[ly - robe[i][1] + y0 - 2][robe[i][0] + 1 - x0] = f'{i}'

        for line in grid:
            f.write(''.join(line) + '\n')

    def move_head(robe, direction):
        if direction == 'R':
            robe[0][0] += 1
        elif direction == 'L':
            robe[0][0] -= 1
        elif direction == 'U':
            robe[0][1] += 1
        elif direction == 'D':
            robe[0][1] -= 1

    def move_tail(robe, knots):
        for i in range(1, knots):
            if abs(robe[i-1][0] - robe[i][0]) > 1 and abs(robe[i-1][1] - robe[i][1]) > 1:
                robe[i][0] = (robe[i - 1][0] + robe[i][0]) // 2
                robe[i][1] = (robe[i - 1][1] + robe[i][1]) // 2
            elif abs(robe[i-1][0] - robe[i][0]) > 1:
                robe[i][0] = (robe[i - 1][0] + robe[i][0])//2
                robe[i][1] = robe[i - 1][1]
            elif abs(robe[i - 1][1] - robe[i][1]) > 1:
                robe[i][1] = (robe[i - 1][1] + robe[i][1]) // 2
                robe[i][0] = robe[i - 1][0]

    def move_robe(knots) -> int:
        robe = [[0, 0] for _ in range(knots)]
        f_out = open(f'day9_out_{knots}knots.txt', 'w')
        visited = []

        for direction, steps in moves:
            steps = int(steps)
            f_out.write(f'\n{direction}{steps}\n')
            for _ in range(steps):
                move_head(robe, direction)
                move_tail(robe, knots)
                visited.append(tuple(robe[-1]))
                print_robe(robe, f_out, knots)

        return len(set(visited))

    return move_robe(2), move_robe(10)


def day_10():
    data_in = data(10)

    register = 1
    states = []
    for line in data_in:
        if line == 'noop':
            states += [register]
        else:
            _, value = line.split(' ')
            states += [register, register]
            register += int(value)

    idx = 19
    signal_strength = 0
    while idx < len(states):
        signal_strength += (idx+1) * states[idx]
        idx += 40

    crt = ''
    for idx, sprite_position in enumerate(states, 1):
        idx = idx % 40
        if idx == 0:
            idx = 40
        if idx == 1:
            crt += '\n'
        if sprite_position <= idx <= (sprite_position + 2):
            crt += 'X'
        else:
            crt += '.'
        if idx % 5 == 0:
            crt += '    '

    print(crt)
    return signal_strength


def day_11():
    data_in = data(11)

    @dataclass
    class MonkeyData:
        items: List[int]
        operation: str
        test_amount: int
        test_monkey_true: int
        test_monkey_false: int
        inspected: int = 0

    MonkeyDataType = Dict[str, List[MonkeyData]]

    monkey_data: MonkeyDataType = {}
    for i in range(0, len(data_in), 7):
        monkey, items, formula, test, test_true, test_false = data_in[i:i + 6]
        monkey = monkey[len('Monkey '):-1]
        monkey_data[monkey] = MonkeyData(
            items=list(map(int, items[len('  Starting items:'):].strip().split(','))),
            operation=formula[len('  Operation: new = '):].strip(),
            test_amount=int(test[len('  Test: divisible by '):]),
            test_monkey_true=test_true[len('    If true: throw to monkey '):],
            test_monkey_false=test_false[len('    If false: throw to monkey '):],
        )

    joint_mod = 1
    for monkey in monkey_data.values():
        joint_mod *= monkey.test_amount

    def process_data(
        rounds: int, monkey_data: MonkeyDataType, divide_3: bool,
    ) -> MonkeyDataType:
        datax = deepcopy(monkey_data)
        for r in range(rounds):
            for n, monkey in datax.items():
                while monkey.items:
                    monkey.inspected += 1
                    old = monkey.items.pop(0)
                    new = eval(monkey.operation)
                    new %= joint_mod
                    if divide_3:
                        new = new // 3
                    if new % monkey.test_amount == 0:
                        datax[monkey.test_monkey_true].items.append(new)
                    else:
                        datax[monkey.test_monkey_false].items.append(new)
        return datax

    def get_business_level(monkey_data: MonkeyDataType)-> int:
        inspected = [monkey.inspected for monkey in monkey_data.values()]
        a, b = sorted(inspected)[-2:]
        return a * b

    data_1 = process_data(20, monkey_data, divide_3=True)
    data_2 = process_data(10000, monkey_data, divide_3=False)

    return get_business_level(data_1), get_business_level(data_2)


def day_12():
    data_in = data(12)

    Y = len(data_in)
    X = len(data_in[0])

    def prepare_grid(start_l: str, stop_l: str):
        grid = {}
        start_points = []
        letter_map = {'S': 'a', 'E': 'z'}
        for x in range(X):
            for y in range(Y):
                point = (x, y)
                letter = data_in[y][x]
                if letter == stop_l:
                    stop_point = (x,y)
                if letter == start_l:
                    start_points.append((x, y))
                    grid[point] = [ord(letter), 0]
                letter = letter_map.get(letter, letter)
                if letter == start_l:
                    start_points.append((x, y))
                    grid[point] = [ord(letter), 0]
                else:
                    grid[point] = [ord(letter), -1]
        return grid, start_points, stop_point

    def print_grid(grid, stop_point, title=None):
        g = f'{title}\n'
        for y in range(Y):
            for x in range(X):
                if (x,y) == stop_point:
                    g += 'X    '
                else:
                    g += (str(grid[(x,y)][1])+chr(grid[(x,y)][0])).ljust(5,' ')
            g += '\n'
        print(g)

    def find(start_from: str):
        grid, start_points, stop_point = prepare_grid(start_from, 'E')
        step = 0
        steps = {0: start_points}

        result = None
        while not result:
            step += 1
            steps[step] = []
            for current in steps[step-1]:
                points = [
                    (current[0]-1, current[1]),
                    (current[0]+1, current[1]),
                    (current[0], current[1]-1),
                    (current[0], current[1]+1),
                ]
                for point in points:
                    # grid edge
                    if point[0] < 0 or point[0] > X -1 or point[1] < 0 or point[1] > Y -1:
                        continue
                    # not eligible path
                    if grid[point][0] - grid[current][0] > 1:
                        continue
                    # visited before
                    if grid[point][1] >= 0:
                        continue
                    if point == stop_point:
                        result = step
                        break

                    # mark as visited with path steps
                    grid[point][1] = step
                    steps[step].append(point)

            if len(steps[step]) == 0 or result:
                break

        print_grid(grid, start_from, title=f'Path from:{start_from}')
        return result
    return find('S'), find('a')


def day_13():
    data_in = data(13, True).strip('\n').split('\n\n')

    pairs = [pair.split('\n') for pair in data_in]
    pairs = [(eval(l), eval(r)) for l, r in pairs]

    def compare(l, r) -> bool:
        if type(l) == type(r) == int:
            if l == r:
                return 0
            else:
                return -1 if l < r else 1

        if type(l) == int:
            l = [l]
        if type(r) == int:
            r = [r]

        for x, y in zip_longest(l, r, fillvalue=-1):
            if x == -1:
                return -1
            if y == -1:
                return 1
            compare_result = compare(x, y)
            if abs(compare_result) == 1:
                return compare_result

        return 0  # compare [] vs []

    counter = 0
    for idx, (x, y) in enumerate(pairs, 1):
        if compare(x, y) == -1:
            counter += idx

    packets = list(chain(*pairs, ([[2]], [[6]])))
    sorted_packets = sorted(packets, key=cmp_to_key(compare))
    result = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)

    return counter, result


def day_14():
    data_in = data(14)

    paths = [
        [
            map(int, position.split(','))
            for position in line.split(' -> ')
        ]
        for line in data_in
    ]

    class GridWithFloor(defaultdict):
        FLOOR = None

        def __missing__(self, key):
            x, y = key
            if y == self.FLOOR:
                return '#'
            else:
                return '.'

    def init_grid(grid: GridWithFloor) -> GridWithFloor:
        for path in paths:
            x_before, y_before = path[0]
            for x, y in path[1:]:
                if x_before == x:
                    for n in range(min(y_before, y), max(y_before, y) + 1):
                        grid_in[x, n] = '#'
                elif y_before == y:
                    for n in range(min(x_before, x), max(x_before, x) + 1):
                        grid_in[n, y] = '#'
                x_before, y_before = x, y

        all_x, all_y = list(zip(*list(grid_in)))
        min_x = min(all_x)
        max_x = max(all_x)
        max_y = max(all_y)

        return grid, (min_x, max_x, max_y)

    def print_grid(grid: GridWithFloor, min_x: int, max_x: int, max_y: int):
        print('Grid', min_x, max_x, max_y, grid.FLOOR)
        for j in range(max_y + 1):
            line = ''
            for i in range(min_x, max_x + 1):
                line += grid[i, j]
            print(line + '\n')

    def run_sand(grid: GridWithFloor, abuse_line: Optional[int] = None) -> int:
        step = 0
        while True:
            x, y = 500, 0
            while True:
                grid[x, y] = '.'
                if grid[x, y + 1] == '.':
                    y += 1
                elif grid[x - 1, y + 1] == '.':
                    y += 1
                    x -= 1
                elif grid[x + 1, y + 1] == '.':
                    y += 1
                    x += 1
                else:
                    grid[x, y] = '+'
                    break
                grid[x, y] = '+'
                if abuse_line and y >= abuse_line:
                    break
            if abuse_line and y >= abuse_line:
                break
            step += 1
            if y == 0:
                break
        return step

    grid_in = GridWithFloor()
    grid_in, (min_x, max_x, max_y) = init_grid(grid_in)

    grid_a = copy(grid_in)
    grid_b = copy(grid_in)
    grid_b.FLOOR = max_y + 2

    step_a = run_sand(grid_a, abuse_line=max_y)
    print_grid(grid_a, min_x, max_x, max_y)
    step_b = run_sand(grid_b)
    print_grid(grid_b, min_x, max_x, max_y + 2)

    return step_a, step_b


if __name__ == '__main__':
    for f in dir():
        if f.startswith('day'):
            print(f'{f}:', getattr(solutions, f)())
