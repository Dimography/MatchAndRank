import sys
sys.path.append('./db_api')
from db_api import database
import matching_alg


def get_mentors(mentee_id):
    db = database("./database/state.db")
    mentee_data = db.get_user_by_id(mentee_id)
    if mentee_data["mentorid"] =='':
        potential_mentors = db.get_by_value("state", "department", mentee_data["department"])
        data = matching_alg.find_mentors(mentee_data, potential_mentors, 5)
        mentor_stat = {}
        for mentor in data.keys():
            mentor_stat.update({mentor: db.generate_out_json(mentor, data[mentor])})
        print(mentor_stat)
        return mentor_stat
    else:
        return False

def choose_mentor(mentor_id, mentee_id):
    db = database("./database/state.db")
    db.set_mentorship_relation(mentor_id, mentee_id)


# 13c630b184f506435e025dd2eccc94975a8028de
# 66b122ab7214ebfa2e82da9d8dcab04af0d6c841
if __name__ == '__main__':
        print(get_mentors("13c630b184f506435e025dd2eccc94975a8028de"))
        choose_mentor("66b122ab7214ebfa2e82da9d8dcab04af0d6c841", "13c630b184f506435e025dd2eccc94975a8028de")
        print(get_mentors("13c630b184f506435e025dd2eccc94975a8028de"))
