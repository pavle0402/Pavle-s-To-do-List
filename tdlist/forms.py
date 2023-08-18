from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, TaskCompletion, Contact
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib import messages

genders = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length= 155, widget=forms.TextInput(attrs={"class":"form-control-sm",
                                                                                "placeholder":"Enter your first name."}))
    last_name = forms.CharField(required=True, max_length= 155, widget=forms.TextInput(attrs={"class":"form-control-sm",
                                                                                "placeholder":"Enter your last name."}))
    username = forms.CharField(required=True, max_length= 155, widget=forms.EmailInput(attrs={"class":"form-control-sm",
                                                                           "placeholder":"Enter your email(username)."}))
    password1 = forms.CharField(required=True, max_length=155, widget=forms.PasswordInput(attrs={"class":"form-control-sm",
                                                                            "placeholder":"Enter your password."}))
    password2 = forms.CharField(required=True, max_length=155, widget=forms.PasswordInput(attrs={"class":"form-control-sm",
                                                                            "placeholder":"Confirm your password."}))
    gender = forms.CharField(required=True, widget=forms.Select(choices=genders, attrs={"class":"form-control-sm"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'password1', 'password2', 'gender') 


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ('task', 'task_due', 'user')

        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Type in your task.'}),
            'user': forms.TextInput(attrs={'class':'form-control','id':'user','value':'', 'type':'hidden'}),
            'task_due': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Vienna timezone. e.g. 12:00'})
        }


class TaskCompletionForm(forms.ModelForm):
    class Meta:
        model = TaskCompletion
        fields = ('task_completion',)
        

        widgets = {
            'task_completion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('topic','email', 'question')

        labels = {
            'topic': 'Topic',
            'question':'Question',
            'email': 'E-mail',
        }

        widgets = {
            'topic': forms.TextInput(attrs={'class':'form-class', 'placeholder':'Topic.'}),
            'question': forms.Textarea(attrs={'class':'form-class', 'placeholder':'Type in your question.', 'cols':50, 'rows':10}),
            'email': forms.EmailInput(attrs={'class':'form-class', 'placeholder':'Type in your email.'}),
        }

        