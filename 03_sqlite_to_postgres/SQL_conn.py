import sqlite3
from dataclasses import dataclass, field, astuple
from contextlib import contextmanager
import uuid


db_path = 'db.sqlite'

@dataclass
class genre:
    id: field(default_factory=uuid.uuid4)
    name: str
    description: str
    created: str
    modified: str

@dataclass
class person:
    id: str
    full_name: str
    created: str
    modified: str

@dataclass
class genre_film_work:
    id: str
    film_work_id: str
    genre_id: str
    created: str

@dataclass
class person_film_work:
    id: str
    film_work_id: str
    person_id: str
    role: str
    created: str

@dataclass
class film_work:
    id: str
    title: str
    description: str
    creation_date: str
    file_path: str
    # certificate: field(default=None)
    rating: field(default=0.0)
    type: str
    created: str
    modified: str

@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn # С конструкцией yield вы познакомитесь в следующем модуле 
    # Пока воспринимайте её как return, после которого код может продолжить выполняться дальше
    conn.close()
    
def slct(rq):
    with conn_context(db_path) as conn:
        curs = conn.cursor()
        curs.execute(f"{rq}")
        result = curs.fetchall()
        return result

def slct_part(table):
    print('Вытаскиваем данные')
    many_dataclasses = []
    with conn_context(db_path) as conn:
            curs = conn.cursor()
            curs.execute(f"SELECT * FROM {table};")
            while True:
                dump = curs.fetchmany(100)
                if not dump:
                    break
                # print(dump)
                for line in dump:
                    line = dict(line)
                    match table:
                        case 'genre':
                            many_dataclasses.append(astuple(genre(id = line["id"], name = line["name"], description = line["description"], created = line["created"], modified = line["modified"]))) # 
                        case 'person':
                            for line in dump:
                                many_dataclasses.append(astuple(person(id = line["id"], full_name = line["full_name"], created = line["created"], modified = line["modified"])))
                        case 'genre_film_work':
                            for line in dump:
                                many_dataclasses.append(astuple(genre_film_work(id = line["id"], film_work_id = line["film_work_id"], genre_id = line["genre_id"], created = line["created"])))
                        case 'person_film_work':
                            for line in dump:
                                many_dataclasses.append(astuple(person_film_work(id = line["id"], film_work_id = line["film_work_id"], person_id = line["person_id"], role = line["role"], created = line["created"])))
                        case 'film_work':
                            for line in dump:
                                many_dataclasses.append(astuple(film_work(id = line["id"], title = line["title"], description = line["description"], creation_date = line["creation_date"], file_path = line["file_path"], rating = line["rating"], type = line["type"], created = line["created"], modified = line["modified"]))) # , certificate = line["certificate"]    
            return many_dataclasses