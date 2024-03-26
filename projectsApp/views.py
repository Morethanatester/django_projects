from django.shortcuts import render
from projectsApp.models import Project

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