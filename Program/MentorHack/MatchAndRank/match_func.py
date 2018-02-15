import numpy as np


def calculate_personal_mentor_possibility(person):
    if (person['wantmentee'] == 1 and len(person['menteeid'].split(', ')) < person['maxmentee']):
        mentor_possibility = person['currentcompanyexperience'] * 0.2 + person['overalexperience'] * 0.1 + person['mentorscore'] * 0.05 - person['ismentor'] * 0.05
    else:
        mentor_possibility = 0
    return mentor_possibility

def calculate_mentor_possibility(mentee, mentor):
    if (mentee['ismentee'] == 1):
        return 0
    if (mentee['department'] != mentor['department']):
        return 0
    if (mentee['id'] == mentor['id']):
        return 0

    if mentee['skills'] == '':
        lang_mathing = 2
    else:
        lang_mathing = 0
        tee_langs = mentee['skills'].split(', ')
        tor_langs = mentor['skills']
        for i in tee_langs:
            if i in tor_langs:
                lang_mathing += 1

    institute_matching = 0
    tee_institutes = mentee['institutes'].split(', ')
    tor_institutes = mentor['institutes']
    for i in tee_institutes:
        if i in tor_institutes:
            institute_matching += 1
            break

    age_diff = abs(mentor['age'] - mentee['age'])

    return calculate_personal_mentor_possibility(mentor) + 0.1 * lang_mathing + 0.1 * institute_matching - 0.01 * age_diff

def find_mentors(mentee, mentors, n):
    matches = []
    for i in mentors:
        matches.append(calculate_mentor_possibility(mentee, i))
    maximum = max(matches)
    maximum = max(10, maximum)
    minimum = min(matches)
    matches = [(i - minimum)/(maximum - minimum) for i in matches]
    matches = np.asarray(matches)
    if (n < len(matches)):
        return matches.argsort()[-n:][::-1]
    else:
        return matches.argsort()[::-1]
