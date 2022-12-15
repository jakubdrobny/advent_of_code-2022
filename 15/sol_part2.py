from dataclasses import dataclass


@dataclass
class Sensor:
    x: int
    y: int
    cx: int
    cy: int

    def __post_init__(self):
        self.radius = abs(self.x - self.cx) + abs(self.y - self.cy)


@dataclass
class Beacon:
    x: int
    y: int


@dataclass
class Interval:
    start: int
    end: int

    def __lt__(self, other):
        return (self.start, self.end) < (other.start, other.end)

    def ln(self):
        return self.end - self.start + 1


def coverage(sensor: Sensor, radius: int, target_row: int) -> Interval:
    dist_to_row = abs(sensor.y - target_row)
    radius_in_row = radius - dist_to_row
    return Interval(sensor.x - radius_in_row, sensor.x + radius_in_row)


def find_possible_source(intervals: list[Interval]) -> int:
    intervals.sort()

    current_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i].start > current_interval.end:
            assert current_interval.end + 2 == intervals[i].start
            return current_interval.end + 1
        else:
            current_interval.end = max(current_interval.end, intervals[i].end)

    return -1


sensors: list[Sensor] = []
with open(input("Enter input file path: "), "r") as f:
    for line in f.readlines():
        line = line.strip("\n").split()

        # parse sensor position
        x = int(line[2].strip(",").split("=")[1])
        y = int(line[3].strip(":").split("=")[1])

        # parse position of closest beacon
        cx = int(line[-2].strip(",").split("=")[1])
        cy = int(line[-1].split("=")[1])

        sensors.append(Sensor(x, y, cx, cy))

MXN: int = int(input("Enter MXN: "))

for row in range(0, MXN + 1):
    # debug
    if row % 100000 == 0:
        print(row)

    intervals: list[Interval] = []
    for sensor in sensors:
        if sensor.radius >= abs(sensor.y - row):
            intervals.append(coverage(sensor, sensor.radius, row))

    source_x = find_possible_source(intervals)

    if source_x == -1:
        continue

    print(source_x * 4000000 + row)
    exit()

# should not get here
assert False
