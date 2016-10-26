from django.http import HttpResponse
from tipz.models import User
from tipz.models import Project
from tipz.models import Pledge

def index(request):
    all_users = User.objects.all()
    all_projects = Project.objects.all()
    all_pledges = Pledge.objects.all()
    html = ''

    for user in all_users:
        url = '/tipz/' + str(user.pk) + '/'
        html += '<a href="' + url + '">' + user.firstname + user.lastname + '</a><br>'

    for project in all_projects:
        url = '/tipz/' + str(project.pk) + '/'
        html += '<a href="' + url + '">' + project.name + '</a><br>'

    for pledge in all_pledges:
        url = '/tipz/' + str(pledge.pk) + '/'
        html += '<a href="' + url + '">' + pledge.title + '</a><br>'
    return HttpResponse(html)

def detail(request, UsersId):
    return HttpResponse("<h2>Details for UsersId: " + str(UsersId) + "</h2>")