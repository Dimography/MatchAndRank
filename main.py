import os
import sys
from db_api.db_api import database
import match_func

def recieve_id():
    return("b047741e5ddfc5e866847ae16e04dc1966502d79")

def main():
    db = database("./database/state.db")
    mentee_id = recieve_id()
    mentee_data = db.get_user_by_id('c2ccf9a4fcb0387a702af6abea8592c5e37ca7cf')
    potential_mentors = db.get_by_value("state", "department", mentee_data["department"])
    data = match_func.find_mentors(mentee_data, potential_mentors, 5)
    print(data)
    return(data)

if __name__ == '__main__':
        main()
