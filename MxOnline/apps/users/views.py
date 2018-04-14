from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile


# class CustomBackend(ModelBackend):
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             user = UserProfile.objects.get(Q(username=username)|())
# # Create your views here.

def login(request):
    if request.method == "POST":
        user_name = request.POST.get.("username", "")
        pass_word = request.POST.get.("password", "")
        user = authenticate(user_name, pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html", {})
        elif:
            return render(request, "login.html", {})

    elif request.method == "GET":
        return render(request, "login.html", {})