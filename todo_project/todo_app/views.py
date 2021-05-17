from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Task
from . forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',{'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')
def task_view(request):
    obj1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date = request.POST.get('date')
        obj=Task(name=name,priority=priority,date=date)
        obj.save()
        return redirect('/')
    return render(request,'task_view.html',{'obj1':obj1})
def delete(request,id):
    if request.method=='POST':
        obj=Task.objects.get(id=id)
        obj.delete()
        return redirect('/')

    return render(request,'delete.html')
def update(request,id):
    obj=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'obj':obj,'form':form})