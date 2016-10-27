from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tipz.models import Pledge
from tipz.models import Project
from tipz.models import User

class IndexView(generic.ListView):
    template_name = 'tipz/index.html'

    def get_queryset(self):
        return Project.objects.all()

class UsersView(generic.ListView):
    template_name = 'tipz/users.html'

    def get_queryset(self):
        return User.objects.all()

class ProjectsView(generic.ListView):
    template_name = 'tipz/projects.html'

    def get_queryset(self):
        return Project.objects.all()

class PledgesView(generic.ListView):
    template_name = 'tipz/pledges.html'

    def get_queryset(self):
        return Pledge.objects.all()

class UsersDetailView(generic.DetailView):
    model = User
    template_name = 'tipz/usersDetail.html'

    def get_queryset(self):
        return User.objects.all()

class ProjectsDetailView(generic.DetailView):
    model = Project
    template_name = 'tipz/projectsDetail.html'

    def get_queryset(self):
        return Project.objects.all()

class PledgesDetailView(generic.DetailView):
    model = Pledge
    template_name = 'tipz/pledgesDetail.html'

    def get_queryset(self):
        return Pledge.objects.all()

class ProjectCreate(CreateView):
    model = Project
    fields = ['name', 'description', 'creationDate', 'owner']