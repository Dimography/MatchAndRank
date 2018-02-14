import sqlite3
import json
DB_PATH = '../database/state.db'

def gen_json_persdata(data):
    with open("{}.json".format(str(person['id'])), "w") as user_json:
        json.dump(person, user_json)

class database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def register_user(self, user_json):
        data = json.load(user_json)
        query = [', '.join(list(map(str, list(data.keys())))), '", "'.join(list(map(str, list(data.values()))))]
        self.cursor.execute('INSERT INTO state ({}) VALUES (\"{}\")'.format(*query))
        self.connection.commit()

    def get_user_by_id(self, id):
        db.cursor.execute("SELECT * from state WHERE id = ?", id)
        data = [dict(db.cursor.fetchone())]
        gen_json_persdata(data)
        return(data)

    def get_user_by_value(self, table, val_name, value):
        db.cursor.execute("SELECT * from {0} where {1} = \'{2}\'".format(table, val_name, value))
        data = [dict(person) for person in db.cursor.fetchall()]
        gen_json_persdata(data)
        return data

    def get_scoring_history(self, id):
        db.cursor.execute("SELECT * from scoring where id = ?", id)
        data = [dict(person) for person in db.cursor.fetchall()]
        gen_json_persdata(data)
        return(data)

    def get_all_data(self, id):
        datalist = {"personal":get_user_by_id(id)}#, "scoring_history":get_scoring_history(id)}
        return gen_json_persdata(datalist)

if __name__ == '__main__':
    db = database(DB_PATH)
    id = str(input())
    
    # with open("user_info.json") as user_data:
        # db.register_user(user_data)
    print(db.get_all_data(id))
