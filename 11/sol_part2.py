from dataclasses import dataclass


def mul(item, item2):
    new_item = {}
    if type(item2) == int:
        for modulo in item:
            value = item[modulo]
            new_item[modulo] = (value * item2) % modulo
    else:
        for modulo in item:
            value = item[modulo]
            new_item[modulo] = (value * value) % modulo
    return new_item


def add(item, item2):
    new_item = {}
    if type(item2) == int:
        for modulo in item:
            value = item[modulo]
            new_item[modulo] = (value + item2) % modulo
    else:
        for modulo in item:
            value = item[modulo]
            new_item[modulo] = (value + value) % modulo
    return new_item


@dataclass
class Monkey:
    id: int
    items_normal: list[int]
    items: list[dict[int]]
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
        items_normal=list(map(int, definition[1].split(": ")[1].split(", "))),
        items=[],
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
modulos = []
for monkey in monkeys:
    modulos.append(monkey.divisibility_test_value)
for monkey in monkeys:
    new_items = []
    for item in monkey.items_normal:
        dictionary = dict()
        for modulo in modulos:
            dictionary[modulo] = item % modulo
        new_items.append(dictionary)
    monkey.items = new_items

for round in range(0, 10000):
    for monkey_index in range(0, len(monkeys)):
        monkey = monkeys[monkey_index]
        for item in monkey.items:
            new_item = {}
            if monkey.operation_operand == "*":
                if monkey.operation_value == "old":
                    new_item = mul(item, item)
                else:
                    new_item = mul(item, int(monkey.operation_value))
            else:
                if monkey.operation_value == "old":
                    new_item = add(item, item)
                else:
                    new_item = add(item, int(monkey.operation_value))
            monkey.items_inspected += 1
            # new_item //= 3
            if new_item[monkey.divisibility_test_value] == 0:
                monkeys[monkey.divisibility_test_success_monkey].items.append(new_item)
            else:
                monkeys[monkey.divisibility_test_failure_monkey].items.append(new_item)
        monkey.items = []

items_inspected = []
for monkey in monkeys:
    items_inspected.append(monkey.items_inspected)
items_inspected.sort()
print(items_inspected[-2] * items_inspected[-1])
