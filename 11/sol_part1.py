from dataclasses import dataclass


@dataclass
class Monkey:
    id: int
    items: list[int]
    operation_operand: str
    operation_value: str
    divisibility_test_value: int
    divisibility_test_success_monkey: int
    divisibility_test_failure_monkey: int
    items_inspected: int = 0


def createMonkey(monkey_string):
    definition = [line.strip(" ") for line in monkey_string.split("\n")]
    return Monkey(
        id=int(definition[0][-2]),
        items=list(map(int, definition[1].split(": ")[1].split(", "))),
        operation_operand=definition[2].split(" ")[-2],
        operation_value=definition[2].split(" ")[-1],
        divisibility_test_value=int(definition[3].split(" ")[-1]),
        divisibility_test_success_monkey=int(definition[4].split(" ")[-1]),
        divisibility_test_failure_monkey=int(definition[5].split(" ")[-1]),
    )


f = open("test.in", "r")
monkeys = f.read().split("\n\n")
f.close()

monkeys = [createMonkey(monkey) for monkey in monkeys]

for round in range(0, 20):
    for monkey_index in range(0, len(monkeys)):
        monkey = monkeys[monkey_index]
        for item in monkey.items:
            new_item = 0
            if monkey.operation_operand == "*":
                if monkey.operation_value == "old":
                    new_item = item * item
                else:
                    new_item = item * int(monkey.operation_value)
            else:
                if monkey.operation_value == "old":
                    new_item = item + item
                else:
                    new_item = item + int(monkey.operation_value)
            monkey.items_inspected += 1
            new_item //= 3
            if new_item % monkey.divisibility_test_value == 0:
                monkeys[monkey.divisibility_test_success_monkey].items.append(new_item)
            else:
                monkeys[monkey.divisibility_test_failure_monkey].items.append(new_item)
        monkey.items = []

items_inspected = []
for monkey in monkeys:
    items_inspected.append(monkey.items_inspected)
items_inspected.sort()
print(items_inspected[-2] * items_inspected[-1])
