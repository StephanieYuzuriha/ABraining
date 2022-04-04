import sqlite3


class Round:
    def __init__(self, id, id_game, id_user, successes,):
        self.id = id
        self.id_game = id_game
        self.id_user = id_user
        self.successes = successes

    def to_dict(self):
        return {"id": self.id,
                "id_game": self.id_game,
                "id_user": self.id_user,
                "successes": self.successes
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
            create table if not exists rounds (
                id varchar PRIMARY KEY,
                id_game varchar,
                id_user varchar,
                successes varchar,
                FOREIGN KEY (id_game) REFERENCES asocia(id)
                FOREIGN KEY (id_user) REFERENCES user(id)
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from round"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        
        round = [Round(**item) for item in data]
        return round

    def save(self, asocia):
        sql = """insert into round (id, id_game, id_user, successes) values (
            :id, :id_game, :id_user, :successes
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, asocia.to_dict())
        conn.commit()
