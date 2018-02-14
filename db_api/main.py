import sqlite3
import json
DB_PATH = '../database/state.db'

def gen_json(data):
    for person in data:
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
        gen_json([dict(db.cursor.fetchone())])

    def get_user_by_value(self, val_name, value):
        db.cursor.execute("SELECT * from state where {0} = \'{1}\'".format(val_name, value))
        gen_json([dict(person) for person in db.cursor.fetchall()])

if __name__ == '__main__':
    db = database(DB_PATH)
    # with open("user_info.json") as user_data:
        # db.register_user(user_data)
    print(db.get_user_by_value("position", "CEO"))
