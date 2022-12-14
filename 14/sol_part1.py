M, N = 300, 700
grid = [["." for j in range(N)] for i in range(M)]
grid[0][500] = "+"

mx_y = 0

for line in open("test.in", "r").readlines():
    line = line.strip().split(" -> ")
    for i in range(1, len(line)):
        sx, sy = map(int, line[i - 1].split(","))
        ex, ey = map(int, line[i].split(","))
        mx_y = max([mx_y, sy, ey])
        if sx == ex:
            if sy > ey:
                sx, sy, ex, ey = ex, ey, sx, sy
            while sy <= ey:
                grid[sy][sx] = "#"
                sy += 1
        else:
            if sx > ex:
                sx, sy, ex, ey = ex, ey, sx, sy
            while sx <= ex:
                grid[sy][sx] = "#"
                sx += 1

cnt = 0
while True:
    x, y = 500, 1
    stopped = False

    while y <= mx_y:
        if grid[y + 1][x] == ".":
            y += 1
        else:
            if grid[y + 1][x - 1] == ".":
                y += 1
                x -= 1
            elif grid[y + 1][x + 1] == ".":
                y += 1
                x += 1
            else:
                stopped = True
                break

    if stopped:
        grid[y][x] = "O"
    else:
        break

    cnt += 1

print(cnt)

f = open("test.out", "w")
for line in grid:
    print("".join(line), file=f)
f.close()
