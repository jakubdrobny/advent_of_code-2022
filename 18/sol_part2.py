from collections import deque

p = {
    tuple(map(int, line.strip("\n").split(",")))
    for line in open("test.in", "r").readlines()
}

dt = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

reachable = set()

N = 40

q = deque()
q.append([0, 0, -1])
reachable.add((0, 0, -1))
while q:
    x, y, z = q.popleft()
    for dx, dy, dz in dt:
        l = [x + dx, y + dy, z + dz]
        if (
            l[0] >= -N
            and l[0] <= N
            and l[1] >= -N
            and l[1] <= N
            and l[2] >= -N
            and l[2] <= N
            and tuple(l) not in reachable
            and tuple(l) not in p
        ):
            reachable.add(tuple(l))
            q.append(l)

cnt = 0
for cp in p:
    l = list(cp)
    for dx, dy, dz in dt:
        tp = (l[0] + dx, l[1] + dy, l[2] + dz)
        if tp not in p:
            if tp in reachable:
                cnt += 1
            else:
                print(tp, "trapped")
print(cnt)
