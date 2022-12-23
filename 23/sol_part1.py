from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Elf:
    id: int
    y: int
    x: int
    direction: int


def print_grid(elves):
    M = 12
    N = 14

    res = [["." for j in range(N)] for i in range(M)]
    for elve in elves:
        res[elve.y][elve.x] = "#"

    for line in res:
        print("".join(line))


delta = [
    [[-1, -1], [-1, 0], [-1, 1]],
    [[1, -1], [1, 0], [1, 1]],
    [[-1, -1], [0, -1], [1, -1]],
    [[-1, 1], [0, 1], [1, 1]],
]
mdy, mdx = [-1, 1, 0, 0], [0, 0, -1, 1]

# intial grid
grid = [line.strip("\n") for line in open("test.in").readlines()]

# grid dimensions
M, N = len(grid), len(grid[0])

# list[Elf]
elves = []
# set[x, y] - taken positions by elves
taken = set()
# total amount of elves
cnt = 0

mn_y, mn_x, mx_y, mx_x = 1000, 1000, 0, 0

# load elves
for row in range(M):
    for col in range(N):
        if grid[row][col] == "#":
            elf = Elf(cnt, row, col, 0)
            elves.append(elf)
            taken.add((col, row))
            cnt += 1

            # update coordinates of smallest rectangle containing all elves
            mn_y = min(mn_y, elf.y)
            mn_x = min(mn_x, elf.x)
            mx_y = max(mx_y, elf.y)
            mx_x = max(mx_x, elf.x)

# simulate rounds
for roundNo in range(10):
    # phase 1
    candidates = []
    new_positions = []
    new_positions_cnt = defaultdict(int)

    # find elves with any adjacent neighbours and that can move
    for index in range(cnt):
        neigh = False
        for _d in delta:
            for dy, dx in _d:
                if (elves[index].x + dx, elves[index].y + dy) in taken:
                    neigh = True
                    break

        # if does not have any neighbours, check if he can move
        if neigh:
            new_direction = -1
            elf = elves[index]

            for direction_cnt in range(4):
                current_direction = (elves[index].direction + direction_cnt) % 4

                clear = True
                for dy, dx in delta[current_direction]:
                    clear = clear and (elf.x + dx, elf.y + dy) not in taken

                if clear:
                    new_direction = current_direction
                    break

            if new_direction != -1:
                candidates.append(index)

                new_position = (elf.x + mdx[new_direction], elf.y + mdy[new_direction])
                new_positions.append(new_position)
                new_positions_cnt[new_position] += 1

    new_candidates = []
    new_new_positions = []
    for candidate_index in range(len(candidates)):
        if new_positions_cnt[new_positions[candidate_index]] == 1:
            new_candidates.append(candidates[candidate_index])
            new_new_positions.append(new_positions[candidate_index])

    new_candidates, candidates = candidates, new_candidates
    new_new_positions, new_positions = new_positions, new_new_positions

    # phase 2
    for index in range(len(candidates)):
        elf = elves[candidates[index]]
        taken.remove((elf.x, elf.y))
        (elf.x, elf.y) = new_positions[index]
        taken.add((elf.x, elf.y))

    for index in range(len(elves)):
        elf = elves[index]
        elves[index].direction = (elves[index].direction + 1) % 4
        mn_y = min(mn_y, elf.y)
        mn_x = min(mn_x, elf.x)
        mx_y = max(mx_y, elf.y)
        mx_x = max(mx_x, elf.x)

print((mx_x - mn_x + 1) * (mx_y - mn_y + 1) - cnt)
