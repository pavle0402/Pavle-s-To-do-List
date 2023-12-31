from typing import List
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Task, TaskCompletion
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm, CreateTaskForm, ContactForm
from django.utils import timezone





def home_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            messages.success(request, f"Hello {user.first_name}, wish you a productive day!")
            return redirect('tasks_list')
        else:
            messages.warning(request, "Incorrect login information, try again.")
            return redirect('home')
    return render(request, 'login.html', {})

def about_page(request):
    return render(request, 'about.html', {})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out. See you soon!")
    return redirect('login')


def register_view(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to our app {user.first_name}!")
            return redirect('tasks_list')
    else:
        form = RegisterUserForm()
    return render(request, "register.html", {'form': form})



class CreateTaskView(CreateView):
    model = Task
    template_name = 'tasks/task_list.html'
    form_class = CreateTaskForm
    success_url = reverse_lazy('tasks_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #just a list of all objects
        context['tasks'] = Task.objects.pinned_first_and_completed_last().filter(user=self.request.user)
        #for stating if unpin all tasks button should appear or not
        context['tasks_pinned'] = Task.objects.filter(pinned=True)
        #for authentication
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return JsonResponse({'status':'success', 'message':'Task created.'})


def task_author_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task_author': task.user
    }
    return render(request, 'tasks/task_list', context)

class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, f"You have successfully deleted selected task.")
        return JsonResponse({'status':'success', 'message':'Task deleted.'})
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    

@require_POST
@login_required
def PinTaskView(request, pk):
    task = Task.objects.get(id=pk)
    try:
        task.pinned = not task.pinned
        task.save()
        return JsonResponse({'status':'success', 'message':'Task pinned.'})
    
    except task.DoesNotExist:
        return JsonResponse({"message":"Non existent object."})


def UnpinAllTasksView(request):
    if request.method == "POST":
        try:
            task = Task.objects.all().update(pinned=False)
            return JsonResponse({'status':'success'})
        except Exception as e:
            return JsonResponse({'status':'error', 'error_message':str(e)})
    else:
        return JsonResponse({'status':'error', 'message':'Invalid request method.'})




@login_required 
def task_completion_view(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error':'Task not found.'})
    
    if request.method == 'POST':
        task_completion, created = TaskCompletion.objects.get_or_create(task_name=task)
        task_completion.task_completion = not task_completion.task_completion
        task_completion.save()
        #updating complete field in Task
        task.complete = task_completion if task_completion.task_completion else None
        task.save()
        messages.success(request, "Task completion status updated.")
        return JsonResponse({'status':'success', 'task_completion':task_completion.task_completion})
    
    return render(request, 'tasks/task_list.html', {})



def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = request.user
            contact.save()
            messages.success(request, f"{request.user.first_name}, you have successfully sent your message. Our team will be quick to answer.")
            return redirect('tasks_list')
        
        else:
            form = ContactForm()
    
    return render(request, 'contact.html', {'form':form})
