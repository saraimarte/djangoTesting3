from django.shortcuts import render
from .models import TodoItem
# Create your views here.

def home(request):
    items = TodoItem.objects.all()
    return render(request, "home.html", {"todos": items})