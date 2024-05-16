from django import forms
from .models import Task

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Your email address',
    'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
    'placeholder': 'Your password',
    'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={
    'placeholder': 'Verify your password',
    'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Your password',
    'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority',]
        exclude = ['user',]


    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'A title for the task',
        'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Add a description',
        'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.Select(attrs={
        'placeholder': 'Set priority',
        'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority','complete']
        exclude = ['user',]


    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'A title for the task',
        'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Add a description',
        'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.Select(attrs={
        'placeholder': 'Set priority',
        'class': 'w-full py-2 px-4 rounded-lg border border-gray-400 mb-4'
    }))
    complete = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'mb-4'
    }))

    
