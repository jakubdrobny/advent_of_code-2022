import ast


def compare(l1, l2, ind):
    if ind == len(l1) and ind == len(l2):
        return 0
    if ind == len(l1):
        return 1
    if ind == len(l2):
        return -1

    if len(l1) and len(l2):
        if type(l1[ind]) == int and type(l2[ind]) == int:
            if l1[ind] == l2[ind]:
                return compare(l1, l2, ind + 1)
            elif l1[ind] < l2[ind]:
                return 1
            else:
                return -1
        else:
            if type(l1[ind]) == int:
                l1[ind] = [l1[ind]]
            elif type(l2[ind]) == int:
                l2[ind] = [l2[ind]]
            ret = compare(l1[ind], l2[ind], 0)
            if ret == 0:
                return compare(l1, l2, ind + 1)
            return ret

    if len(l1) == 0:
        return 1
    if len(l2) == 0:
        return -1
    return 1


ans = 0
index = 1

lines = open("test.in", "r").readlines()

for line_ind in range(0, len(lines), 3):
    l1 = ast.literal_eval(lines[line_ind].strip())
    l2 = ast.literal_eval(lines[line_ind + 1].strip())
    ret = compare(l1, l2, 0)
    if ret == 1:
        ans += index
    index += 1

print(ans)
