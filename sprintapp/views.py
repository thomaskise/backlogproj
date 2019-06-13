from django.shortcuts import render, get_object_or_404
from .models import Status_lkup, Priority_lkup, Points_lkup, Roles_lkup, Story, Task, Teammember, Sprint
from .forms import StoryForm, TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'sprintapp/index.html')

def getbacklog(request):
    story_list=Story.objects.all()
    return render(request, 'sprintapp/backlog.html',{'backlog': story_list})

def getstorydetails(request, id):
    story=get_object_or_404(Story, pk=id)
    taskcount=Task.objects.filter(story=id).count()
    task=Task.objects.filter(story=id)
    context={
        'story' : story,
        'taskcount' : taskcount,
        'task' : task,
    }
    return render(request, 'sprintapp/storydetails.html', context=context)

@login_required
def newstory(request):
    form=StoryForm
    if request.method =='POST':
            form=StoryForm(request.POST)
            if form.is_valid():
                    post=form.save(commit=True)
                    post.save()
                    form=StoryForm() #not required. redisplays empty form
    else: 
            form=StoryForm()
    return render(request, 'sprintapp/newstory.html', {'form' : form})

@login_required
def newtask(request):
        form=TaskForm
        if request.method =='POST':
                form=TaskForm(request.POST)
                if form.is_valid():
                        post=form.save(commit=True)
                        post.save()
                        form=TaskForm() #not required. redisplays empty form
        else: 
                form=TaskForm()
        return render(request, 'sprintapp/newtask.html', {'form' : form})

def loginmessage(request):
        return render(request, 'sprintapp/loginmessage.html')

def logoutmessage(request):
        return render(request, 'sprintapp/logoutmessage.html')