import sqlite3
from Log import slogger


class Database:

    def __init__(self):
        self.data = ""
        self.con = None
        self.cur = None
        slogger(f"Fin __Init__", __name__)

    def connect(self):
        slogger(f"Open Database connection", __name__)
        self.con = sqlite3.connect('./database/Inventaire.db')
        self.cur = self.con.cursor()

    def find_site(self, id_site):
        slogger(f"select * from Lieu where ID='{id_site}'", __name__)
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
            slogger(f"insert into Lieu('ID','Label') values('{id_site}','{label}')", __name__)
            self.cur.execute(f"insert into Lieu('ID','Label') values('{id_site}','{label}')")
            self.con.commit()
            slogger(f"Fin insert_site", __name__)
        except sqlite3.Error as err:
            slogger(f"Exception insert_site : {err}", __name__)

    def find_bien(self, id_site, id_bien):
        slogger(f"select * from BIEN where ID='{id_bien}' and LIEU_ID='{id_site}'", __name__)
        self.cur.execute(f"select * from BIEN where ID='{id_bien}' and LIEU_ID='{id_site}'")
        lst = self.cur.fetchall()
        if len(lst) > 0:
            slogger(f"Fin find_bien = True", __name__)
            return True
        else:
            slogger(f"Fin find_bien = False", __name__)
            return False

    def insert_bien(self, id_site, id_bien, label):
        try:
            slogger(f"insert into BIEN('ID','Label', 'LIEU_ID') values('{id_bien}','{label}','{id_site}')", __name__)
            self.cur.execute(f"insert into BIEN('ID','Label', 'LIEU_ID') values('{id_bien}','{label}','{id_site}')")
            self.con.commit()
            slogger(f"Fin insert_bien", __name__)
        except sqlite3.Error as err:
            slogger(f"Exception insert_bien : {err}", __name__)

    def close(self):
        slogger(f"Database connection close", __name__)
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
