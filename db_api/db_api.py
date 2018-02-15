import sqlite3
import json
import pickle
DB_PATH = '../database/state.db'


class database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def register_user(self, data):
        #data = json.load(user_json)
        query = [', '.join(list(map(str, list(data.keys())))), '", "'.join(list(map(str, list(data.values()))))]
        self.cursor.execute('INSERT INTO state ({}) VALUES (\"{}\")'.format(*query))
        self.connection.commit()

    def get_user_by_id(self, usr_id):
        self.cursor.execute("SELECT * from state WHERE id = \'{}\'".format(usr_id))
        data = dict(self.cursor.fetchone())
        # gen_json(data, "state")
        return(data)

    def get_by_value(self, table, val_name, value):
        self.cursor.execute("SELECT * from {0} where {1} = \'{2}\'".format(table, val_name, value))
        data = [dict(person) for person in self.cursor.fetchall()]
        # gen_json(data, table)
        return(data)

    def get_scoring_history(self, id):
        self.cursor.execute("SELECT * from scoring where id = ?", id)
        data = [dict(person) for person in self.cursor.fetchall()]
        # gen_json(data, scoring)
        return(data)

if __name__ == '__main__':
    db = database(DB_PATH)
    path = str(input(">Relative filepath: "))
    with open(path, "rb") as serialized_arr:
        data_list = pickle.load(serialized_arr)
    for i in data_list:
        for key in i.keys():
            if(type(i[key]) == str):
                i[key] = i[key].replace('"', '')
        db.register_user(i)
