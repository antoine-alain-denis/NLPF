from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from tipz.models import Pledge
from tipz.models import Project
from django.contrib.auth.models import User
from tipz.forms import UserForm
from tipz.forms import LoginForm

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

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', 'description', 'creationDate', 'owner']

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('tipz:index')

class PledgeCreate(CreateView):
    model = Pledge
    fields = ['title', 'description', 'value', 'project', 'investor']

class PledgeUpdate(UpdateView):
    model = Pledge
    fields = ['title', 'description', 'value', 'project', 'investor']

class PledgeDelete(DeleteView):
    model = Pledge
    success_url = reverse_lazy('tipz:index')

class RegisterFormView(View):
    form_class = UserForm
    template_name = 'tipz/register_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('tipz:index')

        return render(request, self.template_name, {'form': form})

class LogoutFormView(View):
    form_class = LoginForm
    template_name = 'tipz/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'tipz/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('tipz:index')
        return render(request, self.template_name, {'form': form})