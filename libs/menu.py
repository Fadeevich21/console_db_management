from libs.service_db import ServiceDB
from typing import List, Callable
from libs.query import Query
from libs.table import Table


class Menu:

    def __init__(self) -> None:
        self.__db = ServiceDB('database/sql.db')
        
        # self.__db.execute_from_file('src/remove_tables.sql')
        # self.__db.execute_from_file('src/create_tables.sql')
        # self.__db.execute_from_file('src/init_tables.sql')
        self.__query = \
        {
            0: 'Выход'
        }

        self.__menu = list()

    def add_query(self, query: Query):
        self.__query[len(self.__query)] = query.name()
        self.__menu.append(query)

    def __choose_menu(self) -> int:
        text = f'Выберите пункт меню:\n'
        for number, name in self.__query.items():
            text += f'{number}. {name}\n'
        text += '_> '
        return int(input(text))

    def handle(self):
        while True:
            choose = self.__choose_menu()
            if choose == 0:
                return
            elif choose > len(self.__menu):
                raise IndexError(f'Ваш выбор {choose} не допустим')

            get_rows_func, columns = lambda: self.__menu[choose - 1].get_rows(self.__db), self.__menu[choose - 1].get_columns()
            Table.write(get_rows_func, columns)