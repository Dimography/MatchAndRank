import sys
sys.path.append('./db_api')
from MatchAndRank.db_api import db_api
from . import matching_alg


def get_mentors(mentee_id):
    db = db_api.database("state.db")
    mentee_data = db.get_user_by_id(mentee_id)
    if mentee_data["mentorid"] =='':
        potential_mentors = db.get_by_value("state", "department", mentee_data["department"])
        data = matching_alg.find_mentors(mentee_data, potential_mentors, 5)
        mentor_stat = {}
        for mentor in data.keys():
            mentor_stat.update({mentor: db.generate_out_json(mentor, data[mentor])})
        return mentor_stat
    else:
        return False


def choose_mentor(mentor_id, mentee_id):
    db = db_api.database("state.db")
    db.set_mentorship_relation(mentor_id, mentee_id)

def get_mentor(mentee_id):
    db = db_api.database("state.db")
    mentee = db.get_user_by_id(mentee_id)
    mentor_id = mentee["mentorid"]
    db.cursor.execute("SELECT name, surname, patronymic, overalexperience, currentcompanyexperience, codinglanguages, age, institutes FROM state WHERE id=\"{}\"".format(mentor_id))
    return(dict(db.cursor.fetchone())
