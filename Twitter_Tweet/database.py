import sqlite3

class Database:

    def __init__(self) -> None:
        # connect to db or create db if not created
        self.con = sqlite3.connect("day96.db")
        self.cur = self.con.cursor()

    def create_table(self):
        # creating tables
        self.cur.execute("CREATE TABLE IF NOT EXISTS IS_GITHUB(FLAG INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS POST_NUM(NUMER INTEGER)")
        self.con.commit()

    def insert_table(self):
        rec = self.cur.execute("SELECT count(1) FROM IS_GITHUB")
        if rec.fetchone()[0] == 0:
            self.cur.execute("INSERT INTO IS_GITHUB VALUES (0)")
            self.con.commit()

        rec = self.cur.execute("SELECT count(1) FROM POST_NUM")
        if rec.fetchone()[0] == 0:
            self.cur.execute("INSERT INTO POST_NUM VALUES (1)")
            self.con.commit()

    def get_is_github(self):
        rec = self.cur.execute("SELECT FLAG FROM IS_GITHUB")
        return rec.fetchone()

    def get_post_num(self):
        rec = self.cur.execute("SELECT NUMER FROM POST_NUM")
        return rec.fetchone()
    
    def update_is_github(self):
        if self.get_is_github()[0] == 0:
            self.cur.execute("UPDATE IS_GITHUB SET FLAG = 1")
        else:
            self.cur.execute("UPDATE IS_GITHUB SET FLAG = 0")
        self.con.commit()

    def update_post_num(self):
        val = self.get_post_num()[0]
        val += 1
        self.cur.execute(f"UPDATE POST_NUM SET NUMER = {val}")
        self.con.commit()
    
    def delete_all_tables(self):
        self.cur.execute("DELETE FROM IS_GITHUB")
        self.cur.execute("DELETE FROM POST_NUM")
        self.con.commit()
    