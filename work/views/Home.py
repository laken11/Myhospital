from django.shortcuts import render, redirect


def index(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'Home.html', context)


def aboutus(request):
    context = {
        "title": "about us"
    }
    return render(request, 'aboutus.html', context)
