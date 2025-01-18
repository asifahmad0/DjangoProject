from django.http import HttpResponse, HttpRequest


def home(request):
    return HttpResponse(request, '<h1>My name is Asif Ahmad</h1>')