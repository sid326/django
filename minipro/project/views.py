from project.models import login
from django.shortcuts import render_to_response
from django.http import HttpResponse

def tagpage(request, tag):
    logins = login.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {"login":login, "tag":tag})
