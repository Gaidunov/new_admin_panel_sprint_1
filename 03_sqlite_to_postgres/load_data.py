from SQL_conn import *
from pSQL_conn import *
from contextlib import contextmanager


if __name__ == '__main__':
    tables = ['film_work', 'genre', 'person', 'person_film_work', 'genre_film_work']
    for table in tables:
        print(table)
        many_dataclasses = slct_part(table)
        match table:
            case 'genre':
                ins_p(table, many_dataclasses)
            case 'person':
                ins_p(table, many_dataclasses)
            case 'genre_film_work':
                ins_p(table, many_dataclasses)
            case 'person_film_work':
                ins_p(table, many_dataclasses)
            case 'film_work':
                ins_p(table, many_dataclasses)
