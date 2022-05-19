import sqlite3
from Log import slogger


class Database:

    def __init__(self):
        self.data = ""
        self.con = None
        self.cur = None
        slogger(f"Fin __Init__", __name__)

    def connect(self):
        self.con = sqlite3.connect('./database/Inventaire.db')
        self.cur = self.con.cursor()
        slogger(f"Fin connect", __name__)

    def find_site(self, id_site):
        self.cur.execute(f"select * from Lieu where ID='{id_site}'")
        lst = self.cur.fetchall()
        if len(lst) > 0:
            slogger(f"Fin find_site = True", __name__)
            return True
        else:
            slogger(f"Fin find_site = False", __name__)
            return False

    def insert_site(self, id_site, label):
        try:
            self.cur.execute(f"insert into Lixeu('ID','Label') values('{id_site}','{label}')")
            self.con.commit()
            slogger(f"Fin insert_site", __name__)
        except sqlite3.Error as err:
            slogger(f"Exception insert_site : {err}", __name__)

    def close(self):
        self.cur.close()
        self.con.close()
        slogger(f"Fin close", __name__)


if __name__ == "__main__":
    print("test")

    data = Database()
    res = data.find_site('55')
    data.close()
    print(res)
else:
    pass
