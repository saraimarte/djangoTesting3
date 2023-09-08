from django.shortcuts import render
from .models import TodoItem, Student
# Create your views here.

def home(request):
    items = TodoItem.objects.all()
    studentItems = Student.objects.all()
    context = {"todos":items, "students":studentItems}
    return render(request, "home.html", context)