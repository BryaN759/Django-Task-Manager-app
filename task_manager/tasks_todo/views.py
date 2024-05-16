from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Task

from .forms import TaskForm, CreateUserForm, LoginForm, CreateTaskForm, EditTaskForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
# Create your views here.


#--------------------- Home page view --------------------------#

def home(request):
    return render(request, 'index.html')


#--------------------- Register page view --------------------------#

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':       
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered Successfully')
            return redirect('login')

    return render(request, 'register.html', {
        'form': form,
    })


#--------------------- Login page view --------------------------#

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('dashboard')
            
    return render(request, 'login.html', {
        'form': form
    })

#--------------------- Logout view --------------------------#

def logout(request):
    auth.logout(request)

    return redirect('home')

#--------------------- Dashboard view --------------------------#

@login_required(login_url='login')
def dashboard(request):

    current_user = request.user.id

    tasks = Task.objects.all().filter(user=current_user)
 

    return render(request, 'profile/dashboard.html', {
        'tasks': tasks,
    })


#--------------------- Add Task view --------------------------#

@login_required(login_url='login')
def createTask(request):
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully')
            return redirect('dashboard')

    return render(request, 'profile/create.html',{
        'form': form,
    })


#--------------------- Edit Task view --------------------------#

@login_required(login_url='login')
def editTask(request, pk):
    task = Task.objects.get(id=pk)

    form = EditTaskForm(instance=task)
    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been updated')
            return redirect('dashboard')

    return render(request, 'profile/edit.html',{
        'form': form,
    })


#--------------------- Delete Task view --------------------------#

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task has been deleted')

        return redirect('dashboard')

    return render(request, 'profile/delete.html',{
        'task': task,
    })

