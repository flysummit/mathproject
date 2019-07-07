from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
def github_views(request):
    t=loader.get_template("mathtest.html")
    html=t.render()
    return HttpResponse(html)
