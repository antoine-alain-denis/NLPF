from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from tipz.models import User
from tipz.models import Project
from tipz.models import Pledge

def index(request):
    all_users = User.objects.all()
    all_projects = Project.objects.all()
    all_pledges = Pledge.objects.all()
    return render(request, 'tipz/index.html',
                  {'all_users': all_users, 'all_projects': all_projects, 'all_pledges': all_pledges})

def users(request):
    all_users = User.objects.all()
    return render(request, 'tipz/users.html', {'all_users': all_users})

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'tipz/projects.html', {'all_projects': all_projects})

def pledges(request):
    all_pledges = Pledge.objects.all()
    return render(request, 'tipz/pledges.html', {'all_pledges': all_pledges})

def usersDetail(request, userId):
    try:
        user = User.objects.get(id = userId)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'tipz/usersDetail.html', {'user': user})

def projectsDetail(request, projectId):
    try:
        project = Project.objects.get(id = projectId)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'tipz/projectsDetail.html', {'project': project})

def pledgesDetail(request, pledgeId):
    try:
        pledge = Pledge.objects.get(id = pledgeId)
    except Pledge.DoesNotExist:
        raise Http404("Pledge does not exist")
    return render(request, 'tipz/pledgesDetail.html', {'pledge': pledge})