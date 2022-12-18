import time

SLAPA = 0
DEBUG = False
DEBUG_LINES = 120
BRUTE = True

max_y = 0
grid = [
    ["+", "-", "-", "-", "-", "-", "-", "-", "+"],
]

for i in range(8100):
    grid.append(["+", ".", ".", ".", ".", ".", ".", ".", "+"])

jets = open("sample.in", "r").readline().strip("\n")
jets_ind = 0

memo_it = dict()
memo_y = dict()
rocks = 7

iteration = 0
while iteration < rocks:
    shape = iteration % 5

    y, x = max_y + 4, 3

    if shape == 0:
        for cnt in range(4):
            grid[y][x + cnt] = "@"

        if DEBUG:
            # for line in grid[:DEBUG_LINES][::-1]:
            # print("".join(line))
            # print()
            time.sleep(SLAPA)

        fell = True

        while fell:
            if jets[jets_ind] == ">":
                if grid[y][x + 4] == ".":
                    grid[y][x] = "."
                    grid[y][x + 4] = "@"
                    x += 1
            else:
                if grid[y][x - 1] == ".":
                    grid[y][x - 1] = "@"
                    grid[y][x + 3] = "."
                    x -= 1
            for cnt in range(4):
                fell = fell and grid[y - 1][x + cnt] == "."

            if fell:
                for cnt in range(4):
                    grid[y - 1][x + cnt] = "@"
                    grid[y][x + cnt] = "."
                y -= 1

            jets_ind = (jets_ind + 1) % len(jets)
            if DEBUG:
                #     for line in grid[:DEBUG_LINES][::-1]:
                #         print("".join(line))
                #     print()
                time.sleep(SLAPA)
        max_y = max(max_y, y)
    elif shape == 1:
        pieces = [
            [y, x + 1],
            [y + 1, x],
            [y + 1, x + 1],
            [y + 1, x + 2],
            [y + 2, x + 1],
        ]
        for py, px in pieces:
            grid[py][px] = "@"

        if DEBUG:
            # for line in grid[:DEBUG_LINES][::-1]:
            # print("".join(line))
            # print()
            time.sleep(SLAPA)

        fell = True

        while fell:
            if jets[jets_ind] == ">":
                if (
                    grid[y][x + 2] == "."
                    and grid[y + 1][x + 3] == "."
                    and grid[y + 2][x + 2] == "."
                ):
                    grid[y][x + 1] = "."
                    grid[y][x + 2] = "@"
                    grid[y + 1][x] = "."
                    grid[y + 1][x + 3] = "@"
                    grid[y + 2][x + 1] = "."
                    grid[y + 2][x + 2] = "@"
                    x += 1
                    for ind in range(5):
                        pieces[ind][1] += 1
            else:
                if (
                    grid[y][x] == "."
                    and grid[y + 1][x - 1] == "."
                    and grid[y + 2][x] == "."
                ):
                    grid[y][x] = "@"
                    grid[y][x + 1] = "."
                    grid[y + 1][x + 2] = "."
                    grid[y + 1][x - 1] = "@"
                    grid[y + 2][x + 1] = "."
                    grid[y + 2][x] = "@"
                    x -= 1
                    for ind in range(5):
                        pieces[ind][1] -= 1

            fell = (
                grid[y][x] == "."
                and grid[y - 1][x + 1] == "."
                and grid[y][x + 2] == "."
            )

            if fell:
                grid[y][x] = "@"
                grid[y + 1][x] = "."
                grid[y - 1][x + 1] = "@"
                grid[y + 2][x + 1] = "."
                grid[y][x + 2] = "@"
                grid[y + 1][x + 2] = "."
                y -= 1

            jets_ind = (jets_ind + 1) % len(jets)
            if DEBUG:
                #                for line in grid[:DEBUG_LINES][::-1]:
                # print("".join(line))
                # print()
                time.sleep(SLAPA)
        max_y = max(max_y, y + 2)
    elif shape == 2:
        pieces = [
            [y, x],
            [y, x + 1],
            [y, x + 2],
            [y + 1, x + 2],
            [y + 2, x + 2],
        ]
        for py, px in pieces:
            grid[py][px] = "@"

        if DEBUG:
            # for line in grid[:DEBUG_LINES][::-1]:
            # print("".join(line))
            # print()
            time.sleep(SLAPA)

        fell = True

        while fell:
            if jets[jets_ind] == ">":
                if (
                    grid[y + 2][x + 3] == "."
                    and grid[y + 1][x + 3] == "."
                    and grid[y][x + 3] == "."
                ):
                    grid[y][x] = "."
                    grid[y][x + 3] = "@"
                    grid[y + 1][x + 2] = "."
                    grid[y + 1][x + 3] = "@"
                    grid[y + 2][x + 2] = "."
                    grid[y + 2][x + 3] = "@"
                    x += 1
                    for ind in range(5):
                        pieces[ind][1] += 1
            else:
                if (
                    grid[y][x - 1] == "."
                    and grid[y + 1][x + 1] == "."
                    and grid[y + 2][x + 1] == "."
                ):
                    grid[y][x - 1] = "@"
                    grid[y][x + 2] = "."
                    grid[y + 1][x + 2] = "."
                    grid[y + 1][x + 1] = "@"
                    grid[y + 2][x + 2] = "."
                    grid[y + 2][x + 1] = "@"
                    x -= 1
                    for ind in range(5):
                        pieces[ind][1] -= 1

            fell = (
                grid[y - 1][x] == "."
                and grid[y - 1][x + 1] == "."
                and grid[y - 1][x + 2] == "."
            )

            if fell:
                grid[y - 1][x] = "@"
                grid[y][x] = "."
                grid[y - 1][x + 1] = "@"
                grid[y][x + 1] = "."
                grid[y - 1][x + 2] = "@"
                grid[y + 2][x + 2] = "."
                y -= 1

            jets_ind = (jets_ind + 1) % len(jets)
            if DEBUG:
                #                for line in grid[:DEBUG_LINES][::-1]:
                # print("".join(line))
                # print()
                time.sleep(SLAPA)
        max_y = max(max_y, y + 2)
    elif shape == 3:
        pieces = [[y, x], [y + 1, x], [y + 2, x], [y + 3, x]]
        for py, px in pieces:
            grid[py][px] = "@"

        if DEBUG:
            # for line in grid[:DEBUG_LINES][::-1]:
            # print("".join(line))
            # print()
            time.sleep(SLAPA)

        fell = True

        while fell:
            if jets[jets_ind] == ">":
                if (
                    grid[y][x + 1] == "."
                    and grid[y + 1][x + 1] == "."
                    and grid[y + 2][x + 1] == "."
                    and grid[y + 3][x + 1] == "."
                ):
                    grid[y][x] = "."
                    grid[y][x + 1] = "@"
                    grid[y + 1][x] = "."
                    grid[y + 1][x + 1] = "@"
                    grid[y + 2][x] = "."
                    grid[y + 2][x + 1] = "@"
                    grid[y + 3][x] = "."
                    grid[y + 3][x + 1] = "@"
                    x += 1
                    for ind in range(len(pieces)):
                        pieces[ind][1] += 1
            else:
                if (
                    grid[y][x - 1] == "."
                    and grid[y + 1][x - 1] == "."
                    and grid[y + 2][x - 1] == "."
                    and grid[y + 3][x - 1] == "."
                ):
                    grid[y][x] = "."
                    grid[y][x - 1] = "@"
                    grid[y + 1][x] = "."
                    grid[y + 1][x - 1] = "@"
                    grid[y + 2][x] = "."
                    grid[y + 2][x - 1] = "@"
                    grid[y + 3][x] = "."
                    grid[y + 3][x - 1] = "@"
                    x -= 1
                    for ind in range(len(pieces)):
                        pieces[ind][1] -= 1

            fell = grid[y - 1][x] == "."

            if fell:
                grid[y - 1][x] = "@"
                grid[y + 3][x] = "."
                y -= 1

            jets_ind = (jets_ind + 1) % len(jets)
            if DEBUG:
                #                for line in grid[:DEBUG_LINES][::-1]:
                # print("".join(line))
                # print()
                time.sleep(SLAPA)
        max_y = max(max_y, y + 3)
    elif shape == 4:
        pieces = [[y, x], [y, x + 1], [y + 1, x], [y + 1, x + 1]]
        for py, px in pieces:
            grid[py][px] = "@"

        if DEBUG:
            # for line in grid[:DEBUG_LINES][::-1]:
            # print("".join(line))
            # print()
            time.sleep(SLAPA)

        fell = True

        while fell:
            if jets[jets_ind] == ">":
                if grid[y][x + 2] == "." and grid[y + 1][x + 2] == ".":
                    grid[y][x] = "."
                    grid[y][x + 2] = "@"
                    grid[y + 1][x] = "."
                    grid[y + 1][x + 2] = "@"
                    x += 1
                    for ind in range(len(pieces)):
                        pieces[ind][1] += 1
            else:
                if grid[y][x - 1] == "." and grid[y + 1][x - 1] == ".":
                    grid[y][x - 1] = "@"
                    grid[y][x + 1] = "."
                    grid[y + 1][x - 1] = "@"
                    grid[y + 1][x + 1] = "."
                    x -= 1
                    for ind in range(len(pieces)):
                        pieces[ind][1] -= 1

            fell = grid[y - 1][x] == "." and grid[y - 1][x + 1] == "."

            if fell:
                grid[y - 1][x] = "@"
                grid[y + 1][x] = "."
                grid[y - 1][x + 1] = "@"
                grid[y + 1][x + 1] = "."
                y -= 1

            jets_ind = (jets_ind + 1) % len(jets)
            if DEBUG:
                #                for line in grid[:DEBUG_LINES][::-1]:
                # print("".join(line))
                # print()
                time.sleep(SLAPA)
        max_y = max(max_y, y + 1)

    iteration += 1
    memo_y[(shape, jets_ind)] = max_y
    memo_it[(shape, jets_ind)] = iteration

    if not BRUTE and (shape, jets_ind) in memo_y:
        print(shape, jets_ind, iteration, max_y)
        print(memo_y[(shape, jets_ind)])
        print(memo_it[(shape, jets_ind)])
        print("memo up up")
        per_cycle_y_gain = max_y - memo_y[(shape, jets_ind)]
        per_cycle_it_count = iteration - memo_it[(shape, jets_ind)]
        iterations_left = rocks - iteration
        full_cycles_left = iterations_left // per_cycle_it_count
        max_y += full_cycles_left * per_cycle_y_gain
        iteration += full_cycles_left * per_cycle_it_count
        print(iterations_left, full_cycles_left)
        print("mxy", max_y)
        print("it", iteration)
        print(per_cycle_y_gain, per_cycle_it_count)

    # for line in grid[:DEBUG_LINES][::-1]:
    #     print("".join(line))
    # print()
    # print(max_y)
    # time.sleep(SLAPA + 3)

# print("jets ind", jets_ind)
print("max_y", max_y)
