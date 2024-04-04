from django.shortcuts import render

# Create your views here

from django.shortcuts import render

def home(request):
    return render(request, "web_pagesApp/home.html", {})

def newhome(request):
    return render(request, "web_pagesApp/newhome.html", {})

'''

***portfolio pages from RealPython***

from web_pagesApp.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projectsApp/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projectsApp/project_details.html", context)

'''

