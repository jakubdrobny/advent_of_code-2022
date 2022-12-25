VALUE = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
DIGITS = "=-012"


def decimal_to_snafu(decimal):
    res = ""

    low, high = "1", "2"
    while decimal > snafu_to_decimal(high):
        low += "="
        high += "2"

    mid = "2" + low[1:]
    res += "1" if decimal <= snafu_to_decimal(mid) else "2"

    power = 5 ** (len(mid) - 2)
    cur = int(res[0]) * power * 5

    low, high = "=" + low[1:-2], high[:-2]

    while power > 0:
        low_decimal, high_decimal = snafu_to_decimal(low), snafu_to_decimal(high)
        for digit in DIGITS:
            new_cur = cur + VALUE[digit] * power
            if (new_cur >= decimal and new_cur + low_decimal <= decimal) or (
                new_cur <= decimal and new_cur + high_decimal >= decimal
            ):
                res += digit
                cur = new_cur
                break
        power //= 5
        low, high = low[:-1], high[:-1]

    return res


def snafu_to_decimal(snafu):
    result = 0
    power = 5 ** (len(snafu) - 1)
    for digit in snafu:
        result += power * VALUE[digit]
        power //= 5
    return result


decimal = 0

for line in open("test.in", "r").readlines():
    snafu = line.strip("\n")
    current_decimal = snafu_to_decimal(snafu)
    decimal += current_decimal

print(decimal_to_snafu(decimal))
