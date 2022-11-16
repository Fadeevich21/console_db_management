from typing import Callable, List


class Table:

    @staticmethod
    def write(func: Callable, columns: List[str]):
        sizes = []
        for column in columns:
            length = len(column)
            if length > 13:
                sizes.append(length + 2)
            else:
                sizes.append(15)
        line = '+' + '=' * (sum(sizes) + len(columns) - 2) + '+\n'
        text = line

        for size, column in zip(sizes, columns):
            text += f'%{size}s' % column + '|'
        text += '\n'
        text += line
        for row in func():
            for size, column in zip(sizes, row):
                text += f'%{size}s' % column + '|'
            text += '\n'
        text += line
        print(text)