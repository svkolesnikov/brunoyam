from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    # return HttpResponse("Hello111")
    return render(response, "main/index.html", {'data': [1, 2, 3], 'title': 'Index2'})


def info(response):
    # return HttpResponse("Hello111")
    return render(response, "main/info.html")
