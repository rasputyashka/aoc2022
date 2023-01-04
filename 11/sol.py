import re
import functools
import operator

monkeys = []

numbers_pattern = r"\d+"


class Monkey:
    def __init__(
        self, self_id, items, op, condition_num, true_reciever, false_reciever
    ):
        self.id = self_id
        self.cnt = 0
        self.items = items
        self.sign = op[0]
        self.right_operand = int(op[1]) if op[1].isdigit() else None
        self.condition_num = condition_num
        self.true_reciever = true_reciever
        self.false_reciever = false_reciever

    def throw(self):
        for el in self.items:
            self.cnt += 1
            if not self.right_operand:
                operand = el
            else:
                operand = self.right_operand
            if self.sign == "+":
                worth = el + operand
            else:
                worth = el * operand
            worth = round(worth // 3)
            if worth % self.condition_num == 0:
                monkeys[self.true_reciever].items.append(worth)
            else:
                monkeys[self.false_reciever].items.append(worth)

        self.items = []

    def __repr__(self):
        return f"id: <{self.id}> items:<{self.items}> true:<{self.true_reciever}, false:{self.false_reciever}> cnt:<{self.cnt}>"


if __name__ == "__main__":
    monkey_id = 0
    monkey_data = []
    for monkey_data in open(0).read().strip().split("\n\n"):
        config = monkey_data.splitlines()
        m_id = int(re.findall(numbers_pattern, config[0])[0])
        m_items = [
            int(item) for item in re.findall(numbers_pattern, config[1])
        ]
        op = config[2][len("  Operation: new = old ") :].split()
        div_by = int(re.findall(numbers_pattern, config[3])[0])
        true_rec = int(re.findall(numbers_pattern, config[4])[0])
        false_rec = int(re.findall(numbers_pattern, config[5])[0])
        monkeys.append(Monkey(m_id, m_items, op, div_by, true_rec, false_rec))

for _ in range(20):
    for monkey in monkeys:
        monkey.throw()

monkeys.sort(key=lambda x: x.cnt)
print(monkeys[-1].cnt * monkeys[-2].cnt)
