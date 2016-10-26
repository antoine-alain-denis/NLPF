from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the tipz app homepage")

def detail(request, UsersPK):
    return HttpResponse("<h2>Details for UsersPK: " + str(UsersPK) + "</h2>")