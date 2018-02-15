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

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * from state WHERE id = \'{}\'".format(user_id))
        data = dict(self.cursor.fetchone())
        # gen_json(data, "state")
        return(data)

    def get_by_value(self, table, val_name, value):
        self.cursor.execute("SELECT * from {0} where {1} = \'{2}\'".format(table, val_name, value))
        data = [dict(person) for person in self.cursor.fetchall()]
        # gen_json(data, table)
        return(data)

    def get_scoring_history(self, user_id):
        self.cursor.execute("SELECT * from scoring where id=?", user_id)
        data = [dict(person) for person in self.cursor.fetchall()]
        # gen_json(data, scoring)
        return(data)

    def generate_out_json(self, user_id, percentage):
        self.cursor.execute("SELECT mentorid FROM state WHERE id=\"{}\"".format(user_id))
        mentee = dict(self.cursor.fetchone())
        self.cursor.execute("SELECT name, surname, patronymic, overalexperience, currentcompanyexperience, codinglanguages, age, institutes FROM state WHERE id=\"{}\"".format(user_id))
        data = dict(self.cursor.fetchone())
        data.update({"percentage":round(percentage)})
        print(data)
        return(data)

    def set_mentorship_relation(self, mentor_id, mentee_id):
        self.cursor.execute("UPDATE state SET menteeid=\"{}\" WHERE id=\"{}\"".format(mentee_id, mentor_id))
        self.cursor.execute("UPDATE state SET mentorid=\"{}\" WHERE id=\"{}\"".format(mentor_id, mentee_id))
        self.connection.commit()


if __name__ == '__main__':
    db = database(DB_PATH)
    # path = str(input(">Relative filepath: "))
    # with open(path, "rb") as serialized_arr:
        # data_list = pickle.load(serialized_arr)
    # for i in data_list:
        # for key in i.keys():
            # if(type(i[key]) == str):
                # i[key] = i[key].replace('"', '')
        # db.register_user(i)

        # 13c630b184f506435e025dd2eccc94975a8028de
        # 66b122ab7214ebfa2e82da9d8dcab04af0d6c841
