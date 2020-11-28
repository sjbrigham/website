from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "home.html")


def bridges(request):
    return render(request, "bridges.html")


def fancy_words(request):
    return render(request, "fancy.html")