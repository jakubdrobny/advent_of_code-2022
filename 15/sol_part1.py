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


def count_beacons_inside(interval: Interval, beacons_positions_on_row: set[int]):
    count = 0
    for position in beacons_positions_on_row:
        if interval.start <= position and position <= interval.end:
            count += 1
    return count


def calculate_union_of_intervals(
    intervals: list[Interval], beacons_positions_on_row: set[int]
):
    intervals.sort()
    answer = 0

    current_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i].start > current_interval.end:
            answer += current_interval.ln()
            print(current_interval)
            current_interval = intervals[i]
        else:
            current_interval.end = max(current_interval.end, intervals[i].end)

    answer += current_interval.ln() - count_beacons_inside(
        current_interval, beacons_positions_on_row
    )
    return answer


ROW: int = int(input("Enter row number to check: "))

sensors: list[Sensor] = []
beacons_positions_on_row: set[int] = set()
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
        if cy == ROW:
            beacons_positions_on_row.add(cy)

intervals: list[Interval] = []
for sensor in sensors:
    if sensor.radius >= abs(sensor.y - ROW):
        intervals.append(coverage(sensor, sensor.radius, ROW))

print(calculate_union_of_intervals(intervals, beacons_positions_on_row))
