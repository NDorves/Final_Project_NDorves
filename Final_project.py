# ПРОЦЕСС РАБОТЫ НАД ПРОЕКТОМ
#  1. Установить тестовую базу у себя на локальном сервере и ознакомиться со
# структурой таблиц и их содержимым, понять связи и типы данных.
# Рекомендуется написать несколько запросов, который выводят фильмы
# определенного жанра и фильмы за определенный год.
# 2. Имея понимание структуры базы и описание сценариев, написать нужные
# запросы на SQL. Приготовьте работающие запросы, которые позже вы будете
# использовать из приложения на Python.
#  3. Напишите запросы, которые сохраняют выбранные ключевые слова, по
# которым осуществлялся поиск, в отдельную таблицу.
# 4. Напишите запросы, которые выводят запросы по популярности - наиболее
# частые выводятся первыми.
# 5. После того, как мы убедились, что запросы работают, начинаем
# проектировать и разрабатывать приложение на Python и интеграция с базой
# данных. Приложение должно запускаться из консоли и работать в
# интерактивном режиме, ожидая ввода команд от пользователя.  Пользователь
# должен вводить команды и получать результаты непосредственно в консоли.
# Нужно подумать, какие модули\классы нужны нашему приложению, как
# разнести логику по разным модулям\классам\функциям. Например, всю
# работу с базой данных можно реализовать отдельным модулем, который
# будет использоваться из модуля работы с пользователем (считывание команд
# с клавиатуры). Также можно вынести отображение результатов в отдельный
# модуль
from search import search_by_keyword, search_by_genre_and_year, save_search_query, get_popular_queries
import string
import time
import sys


def main_final_project():
    while True:
        command = input("Введите для поиска (по ключ.слову: 1; Жанр.год: 2; Популярные: 3.Для выхода:4): ")
        if command == "1":
            keyword = input("Введите ключевое слово: ")
            results = search_by_keyword(keyword)
            save_search_query(keyword)
            for result in results:
                print(result)
        elif command == "2":
            genre = input("Введите жанр: ")
            year = input("Введите год: ")
            results = search_by_genre_and_year(genre, year)
            save_search_query(genre)
            for result in results:
                print(result)
        elif command == "3":
            results = get_popular_queries()
            for result in results:
                print(result)
        elif command == "4":
            print('Вы уже уходите?\n Приятного просмотра \n  и всего Вам доброго!!!')

            text = '  !!!  Finale project morning!!!  '
            temp = ' '

            for i in text:
                if i in string.printable:
                    temp += i
                    print(f'\r   {temp}', end='', flush=True)
                    time.sleep(0.1)

            print()
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main_final_project()

# ================Поиск================Поиск============Поиск========================Поиск===============
# C:\Users\dorve\PycharmProjects\pythonProject2\.venv\Scripts\python.exe C:\Users\dorve\PycharmProjects\pythonProject2\Project_Morning\Final_project.py
# Введите для поиска по ключ.слову-1. Жанр.год-2.Популярные-3. Для выхода-4: 1
# Введите ключевое слово: dark
# ('DARKNESS WAR', 'A Touching Documentary of a Husband And a Hunter who must Escape a Boy in The Sahara Desert')
# ('DARKO DORADO', 'A Stunning Reflection of a Frisbee And a Husband who must Redeem a Dog in New Orleans')
# ('SHANE DARKNESS', 'A Action-Packed Saga of a Moose And a Lumberjack who must Find a Woman in Berlin')
# Введите для поиска по ключ.слову-1. Жанр.год-2.Популярные-3. Для выхода-4: 2
# Введите жанр: family
# Введите год: 2005
# ('Family', 2005, 'JEDI BENEATH', 'A Astounding Reflection of a Explorer And a Dentist who must Pursue a Student in Nigeria')
# ('Family', 2005, 'MOVIE SHAKESPEARE', 'A Insightful Display of a Database Administrator And a Student who must Build a Hunter in Berlin')
# ('Family', 2005, 'REMEMBER DIARY', 'A Insightful Tale of a Technical Writer And a Waitress who must Conquer a Monkey in Ancient India')
# ('Family', 2005, 'RESURRECTION SILVERADO', 'A Epic Yarn of a Robot And a Explorer who must Challenge a Girl in A MySQL Convention')
# ('Family', 2005, 'SPARTACUS CHEAPER', 'A Thrilling Panorama of a Pastry Chef And a Secret Agent who must Overcome a Student in A Manhattan Penthouse')
# Введите для поиска по ключ.слову-1. Жанр.год-2.Популярные-3. Для выхода-4: 3
# ('baby', 18)
# ('', 5)
# ('academy', 4)
# ('AFFAIR PREJUDICE', 3)
# ('horror 2002', 2)
# ('action', 2)
# ('drama 2013', 2)
# ('drama 1999', 2)
# ('chocolate', 2)
# ('drama', 1)
# ('по жанру и году', 1)
# ('поисковый_запрос', 1)
# ('DINOSAUR', 1)
# ('dorado', 1)
# ('australia', 1)
# ('comedy 2010', 1)
# ('2020', 1)
# ('drama 2015', 1)
# ('A Insightful Epistle of a Mad Scientist ', 1)
# ('comedy 2003', 1)
# ('horror 2016', 1)
# ('horror 2005', 1)
# ('pele', 1)
# ('story 2005', 1)
# ('shlyapa', 1)
# ('holy', 1)
# ('babz', 1)
# ('ridgemont', 1)
# ('jellow', 1)
# ('dark', 1)
# ('drama 199', 1)
# ('drama 2005', 1)
# ('dinosauria', 1)
# ('boy', 1)
# ('mama', 1)
# ('drama 2003', 1)
# ('sport 2005', 1)
# ('action 2003', 1)
# ('action 2005', 1)
# ('command', 1)
# ('action 2007', 1)
# ('pil', 1)
# ('hobbit', 1)
# ('holland', 1)
# ('tom', 1)
# ('update sakila.search_queries set query = Null, search_count = nuLL]', 1)
# ('sql', 1)
# ('*', 1)
# ('cruz', 1)
# ('fantasy', 1)
# ('travel', 1)
# ('hobbit on a moon', 1)
# ('pilot', 1)
# ('pilo', 1)
# ('usa', 1)
# ('Astronaut', 1)
# ('robot', 1)
# ('Psychologist', 1)
# ('Waitress', 1)
# ('car', 1)
# ('brad', 1)
# ('thrones', 1)
# ('come', 1)
# ('comed', 1)
# ('f*cking awesome', 1)
# ('thriller', 1)
# ('romantic', 1)
# ('omantic', 1)
# ('romant ', 1)
# ('romant', 1)
# ('cars', 1)
# ('ivanisevic', 1)
# ('bear', 1)
# ('ear', 1)
# ('grills', 1)
# ('space', 1)
# ('alien', 1)
# ('plane', 1)
# ('comedy', 1)
# ('horror', 1)
# ('hobby', 1)
# Введите для поиска по ключ.слову-1. Жанр.год-2.Популярные-3. Для выхода-4: 4
# Вы уже уходите?
#  Приятного просмотра
#   и всего Вам доброго!!!
#
# Process finished with exit code 0