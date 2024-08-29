from django.shortcuts import render, redirect

#3
def index(request):
    if request.user.is_authenticated:
        return redirect("cafe:main")
    else:
        return redirect("users:login")