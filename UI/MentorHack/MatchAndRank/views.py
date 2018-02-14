from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


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
    data = {
        'Mentor': [
            123,
            456,
            789,
        ]
    }

    return JsonResponse(data)


def ajax_FindMentee(request):
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
