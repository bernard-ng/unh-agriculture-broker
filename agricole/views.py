from django.shortcuts import render


def connection(request):
    return render(request, 'login.html')
