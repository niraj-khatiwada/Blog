from django.shortcuts import render

users = [
    {
        'name': "Niraj Khatiwada",
        'age': 23
    },
    {
        'name': "Chandra Kala Khatiwada",
        'age': 40
    },
]


def home(request):
    context = {
        'users': users
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
