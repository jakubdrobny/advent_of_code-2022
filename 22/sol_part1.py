def print_grid(grid):
    for line in grid:
        print(repr("".join(line)))
    print()


def format_commands(line):
    line_length = len(line)

    index = 0
    while line[index].isnumeric():
        index += 1

    res = [line[:index]]

    while index < line_length:
        end_index = index + 1
        while end_index < line_length and line[end_index].isnumeric():
            end_index += 1

        res.append(line[index])
        res.append(line[index + 1 : end_index])

        index = end_index

    return res


f = open("test.in", "r")
lines = f.readlines()
f.close()


ind = lines.index("\n")
grid = lines[:ind]
commands = format_commands(lines[ind + 1])

M = len(grid)
N = 0
for line in grid:
    N = max(N, len(line) - 1)


for index in range(M):
    grid[index] = grid[index][:-1]
    grid[index] = list(grid[index].ljust(N, " "))

cy, cx = 0, 0
while grid[cy][cx] == " ":
    cx += 1

delta_y = [0, 1, 0, -1]
delta_x = [1, 0, -1, 0]
DIRECTIONS = 4
MARK = [">", "v", "<", "^"]
direction = 0


for command_index in range(0, len(commands), 2):
    if command_index - 1 >= 0:
        rotate = 1 if commands[command_index - 1] == "R" else -1
        direction = (direction + rotate + DIRECTIONS) % DIRECTIONS

    for move in range(int(commands[command_index])):
        grid[cy][cx] = MARK[direction]
        ny, nx = cy + delta_y[direction], cx + delta_x[direction]
        if ny < 0 or ny >= M or nx < 0 or nx >= N or grid[ny][nx] == " ":
            ny, nx = cy, cx
            while ny >= 0 and ny < M and nx >= 0 and nx < N and grid[ny][nx] != " ":
                ny -= delta_y[direction]
                nx -= delta_x[direction]
            ny += delta_y[direction]
            nx += delta_x[direction]

        if grid[ny][nx] == "#":
            break

        cy, cx = ny, nx

cy += 1
cx += 1
print(1000 * cy + 4 * cx + direction)
