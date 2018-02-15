import sys
sys.path.append('./db_api')
from db_api import database
import matching_alg

def recieve_id():
    return("0dc1f1f98869ea423b313f499c159c5b04d889ac")

def main():
    db = database("./database/state.db")
    mentee_id = recieve_id()
    mentee_data = db.get_user_by_id(mentee_id)
    potential_mentors = db.get_by_value("state", "department", mentee_data["department"])
    data = matching_alg.find_mentors(mentee_data, potential_mentors, 5)
    mentor_stat = {}
    for mentor in data.keys():
        mentor_stat.update({mentor: db.generate_out_json(mentor, data[mentor])})
    print(mentor_stat)
    return mentor_stat
if __name__ == '__main__':
        main()
