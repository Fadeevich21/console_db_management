from libs.menu import Menu
import libs.query as query


if __name__ == "__main__":
    menu = Menu()
    menu.add_query(query.QueryDisciplines())
    menu.add_query(query.QuerySchedules())
    menu.add_query(query.QueryLvlSettingsDown())
    menu.handle()