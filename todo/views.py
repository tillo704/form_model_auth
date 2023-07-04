from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm,TaskUpdateForm
from django.http import HttpResponse
from  django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class TasksListView(LoginRequiredMixin,ListView):
    login_url = '/users/login/'
    template_name ='main/task/list.html'
    context_object_name = 'tasks'
    paginate_by = 3
 
    def get_queryset(self):
        return Task.objects.filter(author = self.request.user).order_by('-id')


    # def get(self, request):
    #     tasks = Task.objects.filter(author = request.user)
    #     return render(request,'main/task/list.html',{'tasks':tasks})



class TasksCreateView(LoginRequiredMixin,CreateView):
    login_url = '/users/list/'
    template_name ='main/task/create.html'
    form_class = TaskForm
    
    # def get(self,request):
    #     form = TaskForm()
    #     return render(request,'main/task/create.html', {'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('tasks-list') 
        return HttpResponse("New task is not valid")
    





class TasksUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/users/list/'
    template_name ='main/task/update.html'
    form_class = TaskUpdateForm
    queryset = Task.objects.all()
    success_url = reverse_lazy('tasks-list')

    # def get(self,request, pk):
    #     task = get_object_or_404(Task, pk = pk)
    #     form = TaskUpdateForm(instance=task)
    #     return render(request,'main/task/update.html', {'form':form, 'task':task})

    # def post(self,request, pk):
    #     task = get_object_or_404(Task, pk = pk)
    #     form = TaskUpdateForm(instance=task, data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('tasks-list') 
    #     return HttpResponse("Update task is not valid")



class TaskDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/users/login/'
    template_name ='main/task/delete.html'
    queryset = Task.objects.all()
    success_url = reverse_lazy('tasks-list')
  

    # def get(self,request, pk):
    #     task = get_object_or_404(Task,pk=pk)      

    #     return render(request,'main/task/delete.html',{'task': task})
    

    # def post(self,request, pk):
    #     task = get_object_or_404(Task,pk=pk)
    #     task.delete()
    #     return redirect('tasks-list')

