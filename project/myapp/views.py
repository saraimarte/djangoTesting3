from django.shortcuts import render
from .models import TodoItem, Student
# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        grade = request.POST['grade']
        essay = request.POST['essay']

        new_student = Student(name = name, grade = grade, essay = essay)
        new_student.save()

        studentItems = Student.objects.all()
        context = {"students": studentItems}
        return render(request, "home.html", context)
    else:
        return render(request, "home.html")



'''
def home(request):
    items = TodoItem.objects.all()
    studentItems = Student.objects.all()
    context = {"todos":items, "students":studentItems}
    return render(request, "home.html", context)
'''