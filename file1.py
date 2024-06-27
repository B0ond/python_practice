# нужно сделать стак у которого есть методы push(вносим в данные), pop(удаляем и возвращаем), current(текущее значение),
# top(максимальное значение), min_value(минимальное значение)

class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x < self.min_stack[-1]:
            self.min_stack.append(x)

