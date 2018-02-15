from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from MatchAndRank import interface


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
    data = interface.get_mentors(request.user.get_username())

    if (data != False):
        return JsonResponse(data)
    else:
        return JsonResponse({"ERROR, MENTOR ALREADY EXISTS": 1})


def ajax_ChooseMentor(request):
    if (request.GET['mentor']):
        # print("Mentor: ", request.GET['mentor'], "Mentee:", request.user.get_username())
        interface.choose_mentor(request.GET['mentor'], request.user.get_username())

    return JsonResponse({"Complete": True})
