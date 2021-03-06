# from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from steamauth import RedirectToSteamSignIn, GetSteamID64

def index(request):
    return HttpResponse("Hi, Welcome to Test App!")

def login(request):
    return RedirectToSteamSignIn('/process')

def login_process(request):
    steamid = GetSteamID64(request.GET)
    if steamid == False:
        return redirect('/login_failed')
    else:
        print(steamid)
        return redirect('/test_app/')
