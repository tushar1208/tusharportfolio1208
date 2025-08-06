from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    return render(request, 'main/contact.html')

def resume(request):
    return render(request, 'main/resume.html')

def data_visualization(request):
    return render(request, 'main/data_visualization.html')

def python(request):
    return render(request, 'main/python.html')

def machine_learning(request):
    return render(request, 'main/machine_learning.html')

def deep_learning(request):
    return render(request, 'main/deep_learning.html')
