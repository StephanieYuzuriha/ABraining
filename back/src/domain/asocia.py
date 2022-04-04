import sqlite3


class Asocia:
    def __init__(self, id, img_id, description,):
        self.id = id
        self.img_id = img_id
        self.description = description

    def to_dict(self):
        return {"id": self.id,
                "img_id": self.img_id,
                "description": self.description
                }


class InfoRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists asocia (
                id varchar PRIMARY KEY,
                img_id varchar,
                description varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from asocia"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        
        asocia = [Asocia(**item) for item in data]
        return asocia

    def save(self, asocia):
        sql = """insert into asocia (id, img_id, description) values (
            :id, :img_id, :description
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, asocia.to_dict())
        conn.commit()
