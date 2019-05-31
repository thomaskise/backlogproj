from django.shortcuts import render
from .models import Status_lkup, Priority_lkup, Points_lkup, Roles_lkup, Story, Task, Teammember, Sprint

# Create your views here.
def index (request):
    return render(request, 'sprintapp/index.html')

def getbacklog(request):
    story_list=Story.objects.all()
    return render(request, 'sprintapp/backlog.html',{'backlog': story_list})