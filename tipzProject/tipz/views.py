from django.http import HttpResponse
from tipz.models import User

def index(request):
    all_users = User.objects.all()
    html = ''
    for user in all_users:
        url = '/tipz/' + str(user.pk) + '/'
        html += '<a href="' + url + '">' + user.firstname + user.lastname + '</a><br>'
    return HttpResponse(html)

def detail(request, UsersId):
    return HttpResponse("<h2>Details for UsersId: " + str(UsersId) + "</h2>")