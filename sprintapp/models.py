from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Roles_lkup(models.Model):
    rolename=models.CharField(max_length=255)
    rolenamesort=models.SmallIntegerField()
    def __str__(self):
        return self.rolename
    
    class Meta:
        db_table='role'
        verbose_name_plural='roles'

class Points_lkup(models.Model):
    storypoint=models.SmallIntegerField()

    def __num__(self):
        return self.storypoint
    
    class Meta:
        db_table='point'
        verbose_name_plural='points'

class Priority_lkup(models.Model):
    storypriority=models.CharField(max_length=255)
    storyprioritysort=models.SmallIntegerField()

    def __num__(self):
        return self.storypriority
    
    class Meta:
        db_table='priority'
        verbose_name_plural='priorites'

class Status_lkup(models.Model):
    storystatus=models.CharField(max_length=255)
    storystatussort=models.SmallIntegerField()

    def __num__(self):
        return self.storystatus
    
    class Meta:
        db_table='status'
        verbose_name_plural='stati'

class Sprint(models.Model):
    sprintlabel=models.CharField(max_length=255)
    sprintstartdate=models.DateField(null=True, blank=True)
    sprintenddate=models.DateField(null=True, blank=True)
    sprintcomments=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sprintlabel
    
    class Meta:
        db_table='sprint'
        verbose_name_plural='sprints'

class Teammember(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    teammemberrole=models.ForeignKey(Roles_lkup, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.lastname
    
    class Meta:
        db_table='teammember'
        verbose_name_plural='teammembers'

class Story(models.Model):
    storytitle=models.CharField(max_length=255)
    storydetail=models.TextField(null=True, blank=True)
    storyenterdate=models.DateField()
    storyclosedate=models.DateField(null=True, blank=True)
    storypriority=models.ForeignKey(Priority_lkup, on_delete=models.DO_NOTHING)
    storystatus=models.ForeignKey(Status_lkup, on_delete=models.DO_NOTHING)
    storyeffortpoints=models.ForeignKey(Points_lkup, on_delete=models.DO_NOTHING, null=True, blank=True)
    assignedsprint=models.ForeignKey(Sprint, on_delete=models.DO_NOTHING)
    ownerproduct=models.ForeignKey(Teammember, related_name='stakeholder', on_delete=models.DO_NOTHING)
    ownersprintteam=models.ForeignKey(Teammember, related_name='technicalowner', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.storytitle
    
    class Meta:
        db_table='story'
        verbose_name_plural='stories'

class Task(models.Model):
    tasktitle=models.CharField(max_length=255)
    story=models.ForeignKey(Story, on_delete=models.DO_NOTHING)
    Teammembermember=models.ManyToManyField(Teammember)
    taskdetails=models.TextField(null=True, blank=True)
    taskefforttime=models.DecimalField(decimal_places=2,max_digits=4, null=True, blank=True)

    def __str__(self):
        return self.tasktitle
    
    class Meta:
        db_table='task'
        verbose_name_plural='tasks'
