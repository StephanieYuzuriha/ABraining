import sqlite3

class Round:
    def __init__(self, game_name, wrong_matches, date, id_user = ""):
        self.game_name = game_name
        self.wrong_matches = wrong_matches
        self.id_user = id_user
        self.date = date
        

    def to_dict(self):
        return {
                "game_name": self.game_name,
                "id_user": self.id_user,
                "wrong_matches": self.wrong_matches,
                "date" : self.date
                }


class RoundsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE if not exists rounds (
                game_name varchar,
                id_user varchar,
                wrong_matches varchar,
                date date,
               
                FOREIGN KEY (id_user) REFERENCES user(id)
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    
    def get_all_rounds_by_user(self, id_user):
        sql = """SELECT * FROM rounds WHERE id_user =:id_user"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id_user" : id_user})

        data = cursor.fetchall()
        
        round = [Round(**item) for item in data]
        return round
    
    def save(self, round):
        if round.wrong_matches == "":
            round.wrong_matches = "0"
            
        sql = """INSERT INTO rounds (game_name, id_user, wrong_matches, date ) values (
            :game_name, :id_user, :wrong_matches, :date
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, round.to_dict())
        conn.commit()
    
    # def get_game_numer(self, id_user):
    #     sql ="""SELECT MAX(game_numer) FROM rounds WHERE id_user =:id_user"""
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(sql)
    #     data = cursor.fetchall()
        
    #     return data
        