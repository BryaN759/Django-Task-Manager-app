
import os
from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Task

from .forms import CreateUserForm, LoginForm, CreateTaskForm, EditTaskForm, ProfileForm

from django.contrib.auth.models import auth, User

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
    messages.success(request, 'Logged out successfully')
    return redirect('home')

#--------------------- Dashboard view --------------------------#

@login_required(login_url='login')
def dashboard(request):

    current_user = request.user.id

    tasks = Task.objects.all().filter(user=current_user)


    return render(request, 'profile/dashboard.html', {
        'tasks': tasks,
    })

#--------------------- Clear incomplete tasks view --------------------------#

@login_required(login_url='login')
def clear_incomplete_tasks(request):
    current_user = request.user
    incomplete_tasks = Task.objects.filter(user=current_user, complete=False)
    if request.method == 'POST':

        for task in incomplete_tasks:
            if task.images:
                os.remove(task.images.path)

        incomplete_tasks.delete()
        messages.success(request, 'Incomplete tasks cleared successfully.')
        return redirect('dashboard')

    return render(request, 'profile/prompt.html', {
        'incomplete_tasks': incomplete_tasks,
    })


#--------------------- Clear complete tasks view --------------------------#

@login_required(login_url='login')
def clear_complete_tasks(request):
    complete_tasks = Task.objects.filter(user=current_user, complete=True)
    current_user = request.user
    if request.method == 'POST':

        for task in complete_tasks:
            if task.images:
                os.remove(task.images.path)
            
        complete_tasks.delete()
        messages.success(request, 'Complete tasks cleared successfully.')
        return redirect('dashboard')

    return render(request, 'profile/prompt.html', {
        'complete_tasks': complete_tasks,
    })


#--------------------- Clear complete tasks view --------------------------#

@login_required(login_url='login')
def clear_all_tasks(request):
    current_user = request.user
    all_tasks = Task.objects.filter(user=current_user)
    if request.method == 'POST':

        for task in all_tasks:
            if task.images:
                os.remove(task.images.path)

        all_tasks.delete()
        messages.success(request, 'All tasks has been deleted')
        return redirect('profile')
    
    return render(request, 'profile/prompt.html', {
        'all_tasks': all_tasks,
    })


#--------------------- Profile view --------------------------#

@login_required(login_url='login')
def profile(request):
    current_user = request.user.id
    tasks = Task.objects.all().filter(user=current_user)

    if request.method == 'POST':
        user_form = ProfileForm(request.POST, instance=request.user)
        if user_form.is_valid:
            user_form.save()

            messages.success(request, 'Profile updated successfully')

            return redirect('profile')
        
    user_form = ProfileForm(instance=request.user)

    return render(request, 'profile/profile.html', {
        'user_form': user_form,
        'tasks': tasks,
    })


#--------------------- Delete Profile view --------------------------#

@login_required(login_url='login')
def deleteProfile(request):
    current_user = request.user.username
    if request.method == 'POST':
        deleteUser = User.objects.get(username=request.user)
        deleteUser.delete()
        messages.success(request, 'Profile deleted successfully')
        return redirect('home')
        


    return render(request, 'profile/delete-profile.html')



#--------------------- Add Task view --------------------------#

@login_required(login_url='login')
def createTask(request):
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, request.FILES)

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
        form = EditTaskForm(request.POST, request.FILES, instance=task)

        if form.is_valid():
            task = form.save(commit=False)
            if 'images' in request.FILES:
                if task.images:
                    os.remove(task.images.path)
                task.images = request.FILES['images']

            task.save()
            messages.success(request, 'Task has been updated')
            return redirect('dashboard')
    
        
    return render(request, 'profile/edit.html',{
        'form': form,
    })


#--------------------- Delete Task view --------------------------#

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        if task.images:
            os.remove(task.images.path)
        task.delete()
        messages.success(request, 'Task has been deleted')

        return redirect('dashboard')

    return render(request, 'profile/delete.html',{
        'task': task,
    })


#--------------------- Search Task view --------------------------#

@login_required(login_url='login')
def searchTask(request):
    tasks = tasks = Task.objects.filter(user=request.user)
    search_query = request.GET.get('search_query')

    if search_query:  # If there's a search query, filter tasks based on it
        search_tasks = tasks.filter(title__icontains=search_query)
    else:
        search_tasks = None  # No search query, so set search_tasks to None

    return render(request, 'profile/dashboard.html', {'tasks': tasks, 'search_tasks': search_tasks, 'search_query': search_query})

    

