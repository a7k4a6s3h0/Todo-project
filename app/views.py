from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic, View
from .dj_forms import *
from . models import *

# Create your views here.

def main_view(request):
    task_instance = User_Tasks.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Task Created Successfully...!!!')
            return redirect('/')
        else:
            print("form is not valid", form.errors)
            messages.error(request,'something went worng...!!!')
            
    return render(request, 'home.html',{'task_instance':task_instance})


def Task_update_View(request, slug):
    task_instance = get_object_or_404(User_Tasks, slug=slug)
    old_name  = task_instance.task_name
    if request.method == 'POST':

        form = UpdateTaskForm(data=request.POST, instance=task_instance)
        if form.is_valid():
            form.save()
            messages.success(request,f'Task {old_name} Updated Successfully...!!!')
            return redirect('/')
        else:
            print("form is not valid", form.errors)
            messages.error(request,'something went worng...!!!')

    return render(request, 'update.html', {'task_instance':task_instance})


def Delete_Task(request):
    slug = request.GET.get('value')
    task_instance = get_object_or_404(User_Tasks, slug=slug)
    task_instance.delete()
    return JsonResponse({
        "status": 201,
        "message":"Task deleted successfully"
    })



# <.......................CLASS BASED VIEWS.............................>


class HomeView(generic.ListView):

    model = User_Tasks
    template_name = 'home.html'
    context_object_name = 'task_instance'
    ordering = ['-created_at']

    def post(self, request):
        
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Task Created Successfully...!!!')
            return redirect('/')
        else:
            print("form is not valid", form.errors)
            messages.error(request,'something went worng...!!!')

        return super().get(request)        
    
class UpdateTaskView(generic.UpdateView):

    model = User_Tasks
    template_name = 'update.html'
    fields = ['task_name', 'task_describtion']
    context_object_name = 'task_instance'
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        old_name = self.get_object().task_name
        messages.success(self.request, f'Task {old_name} Updated Successfully...!!!')
        return super().form_valid(form)
    
class DeleteTaskView(View):

    def get(self, request):
            slug = request.GET.get('value')
            task_instance = get_object_or_404(User_Tasks, slug=slug)
            task_instance.delete()
            return JsonResponse({
                "status": 201,
                "message": "Task deleted successfully"
            })