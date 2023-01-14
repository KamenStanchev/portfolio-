from django.shortcuts import render

from portfolio_app.models import Project


def home(request):
    return render(request, 'home.html')


def projects_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects-list.html', context)


def project_details(request, pk):
    project = Project.objects.get(id=pk)
    contex = {'project': project}
    return render(request, 'project-details.html', contex)
