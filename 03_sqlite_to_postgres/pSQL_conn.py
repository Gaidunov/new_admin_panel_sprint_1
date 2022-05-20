import psycopg2
import os
from psycopg2.extras import execute_batch

dsn = {
    'dbname': 'movies_database',
    'user': 'app',
    'password': '123',
    'host': 'localhost',
    'port': 5432,
    'options': '-c search_path=content',
}

def ins_p(table, many_dataclasses):
    match table:
        case 'genre':
            with psycopg2.connect(**dsn) as conn, conn.cursor() as cur:
                query = 'INSERT INTO content.genre (id, name, description, created, modified) VALUES (%s,%s,%s,%s,%s) ON CONFLICT (id) DO NOTHING'
                execute_batch(cur, query, many_dataclasses, 10)
                conn.commit()
                cur.execute('select count(*) from content.genre;')
                if cur.fetchall()[0][0] == len(many_dataclasses):
                    True
        case 'person':
            with psycopg2.connect(**dsn) as conn, conn.cursor() as cur:
                query = 'INSERT INTO content.person (id, full_name, created, modified) VALUES (%s,%s,%s,%s) ON CONFLICT (id) DO NOTHING'
                execute_batch(cur, query, many_dataclasses, 1000)
                conn.commit()
                cur.execute('select count(*) from content.person;')
                if cur.fetchall()[0][0] == 4166:
                    True
        case 'genre_film_work':
            with psycopg2.connect(**dsn) as conn, conn.cursor() as cur:
                query = 'INSERT INTO content.genre_film_work (id, film_work_id, genre_id, created) VALUES (%s,%s,%s,%s) ON CONFLICT (id) DO NOTHING'
                execute_batch(cur, query, many_dataclasses, 1000)
                conn.commit()
                cur.execute('select count(*) from content.genre_film_work;')
                if cur.fetchall()[0][0] == 2231:
                    True
        case 'person_film_work':
            with psycopg2.connect(**dsn) as conn, conn.cursor() as cur:
                query = 'INSERT INTO content.person_filmwork (id, film_work_id, person_id, role, created) VALUES (%s,%s,%s,%s,%s) ON CONFLICT (id) DO NOTHING'
                execute_batch(cur, query, many_dataclasses, 1000)
                conn.commit()
                cur.execute('select count(*) from content.person_filmwork;')
                if cur.fetchall()[0][0] == 5783:
                    True
        case 'film_work':
            with psycopg2.connect(**dsn) as conn, conn.cursor() as cur:
                query = 'INSERT INTO content.filmwork (id, title, description, creation_date, file_path, rating, type, created, modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (id) DO NOTHING'
                execute_batch(cur, query, many_dataclasses, 1000)
                conn.commit()
                cur.execute('select count(*) from content.filmwork;')
                if cur.fetchall()[0][0] == 999:
                    True


