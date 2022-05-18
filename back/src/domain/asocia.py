import sqlite3
import random

class AsociaQuestion:
    def __init__(self, img_id, description, id=None, show = True):
        self.id = id
        self.img_id = img_id
        self.description = description
        self.show = show

    def to_dict(self):
        return {"id": self.id,
                "img_id": self.img_id,
                "description": self.description,
                "show": self.show
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
            CREATE TABLE if not exists asocia (
                id INTEGER PRIMARY KEY AutoIncrement,
                img_id VARCHAR,
                description VARCHAR,
                show BOOLEAN
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
    
    def get_asocia_img_with_id(self):
        sql = """SELECT id, img_id FROM asocia"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        
        data = cursor.fetchall()
       
        img_list = [item for item in data]
        
        return img_list
    
    def get_asocia_desc_with_id(self):
        sql = """SELECT id, description FROM asocia"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        
        data = cursor.fetchall()
       
        desc_list_dict = [item for item in data]
        
        return desc_list_dict
    
    def make_random_asocia_list(img, desc):
        random_list=[]
        random_img = random.choices(img )
        random_desc = random.choices(desc)
        for img, desc in random_img and random_desc:
            random_list.append([{"img_id":img, "description":desc}])
            
        return random_list    

    def save(self, asocia):
        sql = """INSERT INTO asocia ( img_id, description, show) VALUES (
             :img_id, :description, "true"
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, asocia.to_dict())
        conn.commit()
        
        return

