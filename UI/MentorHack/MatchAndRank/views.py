from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .db_api import db_api
from . import match_func

# Main page
def main(request):
    return render(request, 'MatchAndRank/Main.html')


def logOut(request):
    logout(request)
    return render(request, 'MatchAndRank/Main.html')


@login_required(login_url="login")
def account(request):
    return render(request, 'MatchAndRank/Account.html')


@login_required(login_url="login")
def findMentor(request):
    return render(request, 'MatchAndRank/FindMentor.html')


@login_required(login_url="login")
def findMentee(request):
    return render(request, 'MatchAndRank/FindMentee.html')


def ajax_FindMentor(request):
    db = db_api.database("state.db")
    mentee_id = request.user.get_username()
    mentee_data = db.get_user_by_id(mentee_id)
    potential_mentors = db.get_by_value("state", "department", mentee_data["department"])
    data = match_func.find_mentors(mentee_data, potential_mentors, 5)
    print(data)

    return JsonResponse({"123": 223})


def ajax_FindMentee(request):
    id = request.user.get_username()

    data = {
        'Mentee': [
            123,
            456,
            789,
        ]
    }

    return JsonResponse(data)


# Sending data to web-page
def ajax_GetUserData(request):
    id = request.user.get_username()

    data = {
        'fields': {
            'must': [
                'name',
                'id',
                'position'
            ],
        }
    }

    return JsonResponse(data)
