
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegisterForm,LoginForm
from django.http import HttpResponse
from django.core.mail import send_mail
from todo_app import settings

from .models import Tasks,Register,Login
# Create your views here.

class TaskList(ListView):
    model= Tasks
    context_object_name = 'task1'
    template_name = 'tasklist.html'

class TaskCreate(CreateView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'

class TaskUpdate(UpdateView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'

class TaskDelete(DeleteView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model=Tasks
    fields='__all__'
    success_url=reverse_lazy('task1')
    template_name = 'taskdetail.html'


def register_fun(request):
    register=Register.objects.all()
    form=RegisterForm()

    if request.method=='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login/')
    context={'register':register,'form':form}
    return render(request,'register.html',context)


def login_fun(request):
    login=Login.objects.all()
    form=LoginForm()

    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/task-list/')
    context={'login':login,'form':form}
    return render(request,'login.html',context)

def home(request):
    template="home.html"
    context={}
    return render(request,template,context)

def mail(request):
    subject="Greetings"
    msg="Congratulations for Your Success"
    to="sreelakshmic222@gmail.com"
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if res==1:
        msg="Mail sent Successfully"
    else:
        msg="Mail could not sent"
    return HttpResponse(msg)
