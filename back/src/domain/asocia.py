import sqlite3


class AsociaQuestion:
    def __init__(self, img_id, description, id=None):
        self.id = id
        self.img_id = img_id
        self.description = description

    def to_dict(self):
        return {"id": self.id,
                "img_id": self.img_id,
                "description": self.description
                }


class AsociaRepository:
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
                id INTEGER PRIMARY KEY AutoIncrement,
                img_id varchar,
                description varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_asocia_game(self):
        sql = """SELECT * FROM asocia"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        
        data = cursor.fetchall()
       
        asocia = [AsociaQuestion(**item) for item in data]
        
        return asocia
    
    def get_asocia_img(self):
        sql = """SELECT img_id FROM asocia"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        
        data = cursor.fetchall()
       
        asocia = [item for item in data]
        
        return asocia

    def save(self, asocia):
        sql = """INSERT INTO asocia ( img_id, description) VALUES (
             :img_id, :description
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, asocia.to_dict())
        conn.commit()
        
        return
