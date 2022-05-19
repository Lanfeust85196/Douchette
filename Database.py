import sqlite3
import Log


class Database:

    def __init__(self):
        self.data = ""
        self.con = None
        self.cur = None
        logger.debug(f"__Init__")

    def connect(self):
        self.con = sqlite3.connect('./database/Inventaire.db')
        self.cur = self.con.cursor()

    def find_site(self, id_site):
        self.cur.execute(f"select * from Lieu where ID='{id_site}'")
        lst = self.cur.fetchall()
        if len(lst) > 0:
            return True
        else:
            return False

    def insert_site(self, id_site, label):
        try:
            self.cur.execute(f"insert into Lieu('ID','Label') values('{id_site}','{label}')")
            self.con.commit()
        except sqlite3.Error as err:
            print(err.sqlite_errorname)

    def close(self):
        self.cur.close()
        self.con.close()


if __name__ == "__main__":
    print("test")

    data = Database()
    res = data.find_site('55')
    data.close()
    print(res)
else:
    pass
