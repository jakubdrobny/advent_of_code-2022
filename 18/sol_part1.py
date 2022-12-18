p = {
    tuple(map(int, line.strip("\n").split(",")))
    for line in open("test.in", "r").readlines()
}

dt = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

cnt = 0

for cp in p:
    l = list(cp)
    for dx, dy, dz in dt:
        tp = (l[0] + dx, l[1] + dy, l[2] + dz)
        if tp not in p:
            cnt += 1

print(cnt)
