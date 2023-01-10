from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from . models import Tasks

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
def index(request):
    if request.method == 'POST':
        task_name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Tasks(task_name=task_name,priority=priority,date=date)
        task.save()
    tasks = Tasks.objects.all()
    return render(request,'index.html',{'task1':tasks})

# def details(request):
#     tasks = Tasks.objects.all()
#     return render(request,'details.html',{'task':tasks})
def delete(request,taskid):
    if request.method == 'POST':
        task = Tasks.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task = Tasks.objects.get(id=id)
    f = TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})


# class based generic views
class Tasklistview(ListView):
    model = Tasks
    template_name = 'index.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model = Tasks
    template_name = 'details.html'
    context_object_name = 'task'
class Taskupdate(UpdateView):
    model = Tasks
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('task_name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class Taskdeleteview(DeleteView):
    model = Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvindex')