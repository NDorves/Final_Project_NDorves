# PROJECT MORNING
#   - Создание консольного приложения для поиска фильмов по базе данных sakila
#
# ЦЕЛЬ ПРОЕКТА
#  Реализовать сценарии поиска фильмов:
#       ● По ключевому слову находится 10 фильмов.
#       ● По жанру и году находится 10 фильмов.
#       ● По команде выводится список самых популярных запросов, по которым был поиск.
# Так же  добавлены критерии поиска фильмов
#         * по имени актёра
#         * по фамилии актёра

#
#
from search import (search_by_keyword, search_by_genre, search_by_year,
                    search_by_actor_name1, search_by_actor_name2, save_search_query, get_popular_queries)
import string
import time


def final_project():
    while True:
        command = input("Код поиска:"
                        "\n1 - название фильма,  2 - год,\n3 - Жанр,"
                        "             4 - имя актёра,        44 - фамилию актёра,\n5 - топ популярных,  "
                        " 6 - Для выхода  из поиска.\n_______________________________________"
                        " \nВведите код поиска: ")
        if command == "1":
            keyword = input("Введите ключевое слово: ")
            results = search_by_keyword(keyword)
            save_search_query(keyword)
            for result in results:
                print(result)


        elif command == "2":
            year = input("Введите год: ")
            results = search_by_year(year)
            save_search_query(year)
            for result in results:
                print(result)

        elif command == "3":
            genre = input("Введите жанр: ")
            results = search_by_genre(genre)
            save_search_query(genre)
            for result in results:
                print(result)

        elif command == "4":
            Actor = input("Введите имя актёра: ")
            results = search_by_actor_name1(Actor,)
            save_search_query(Actor)
            for result in results:
                print(result)

        elif command == "44":
            name = input("Введите фамилию актёра: ")
            results = search_by_actor_name2(name,)
            save_search_query(name)
            for result in results:
                print(result)

        elif command == "5":
            results = get_popular_queries()
            for result in results:
                print(result)
        elif command == "6":
            print('Приятного просмотра \n  и всего Вам доброго!!!')

            text = '  !!!  Finale project MORNING  !!!  '
            temp = ' '

            for i in text:
                if i in string.printable:
                    temp += i
                    print(f'\r   {temp}', end='', flush=True)
                    time.sleep(0.1)

            print()
            break


        else:
            print("Неизвестная команда,\n       уточните команду и повторите попытку! ")


if __name__ == "__main__":
    final_project()
