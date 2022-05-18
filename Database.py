import sqlite3


class Database:

    def __init__(self):
        self.con = sqlite3.connect('./database/Inventaire.db')
        self.cur = self.con.cursor()

    def select_lieu(self):
        self.cur.execute("select * from Lieu")
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.con.close()


if __name__ == "__main__":
    print("test")

    data = Database()
    res = data.select_lieu()
    data.close()
    print(res)
else:
    pass
