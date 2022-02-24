
from student.filters import ActivityFilter
from django.shortcuts import render
from student.forms import ActivityForm,ProgramForm, ProfessorForm, CentreForm
from student.models import Activity
from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)



def index(request):
    context ={}
  
    # create object of form
    form = ActivityForm(request.POST)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
  
    context['form']= form
    return render(request, "student/index.html", context)

def program(request):
    context ={}
  
    # create object of form
    form = ProgramForm(request.POST)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
  
    context['form']= form
    return render(request, "student/program.html", context)

def centre(request):
    context ={}
  
    # create object of form
    form = CentreForm(request.POST)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
  
    context['form']= form
    return render(request, "student/centre.html", context)

def professor(request):
    context ={}
  
    # create object of form
    form = ProfessorForm(request.POST)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
  
    context['form']= form
    return render(request, "student/professor.html", context)


def TimeTableView(request):

    students = Activity.objects.all().order_by('start_time')     # DB hit once only
    
    filter = ActivityFilter(request.GET, queryset= students)
    
           
    return render(request, 'student/TimeTable.html', {'students':students, 'filter': filter})

def delete_activity(request,pk):
    students = Activity.objects.all().order_by('start_time')
    if request.method == "POST" or request.method == "DELETE":
        
        Activity.objects.filter(pk=pk).delete()
        
    return redirect('Timetable')
