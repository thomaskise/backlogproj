from django import forms
from .models import Status_lkup, Priority_lkup, Points_lkup, Roles_lkup, Story, Task, Teammember, Sprint

class StoryForm(forms.ModelForm):
    class Meta:
        model=Story
        fields='__all__'
        #can list individual fields seperated by a comma
        #also definition of form fields

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        #can list individual fields seperated by a comma
        #also definition of form fields