import sys
sys.path.append('./db_api')
from db_api import database
import matching_alg


def main(mentee_id):
    db = database("./database/state.db")
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
