from django.contrib import admin
from .models import Status_lkup, Priority_lkup, Points_lkup, Roles_lkup, Story, Task, Teammember, Sprint

# Register your models here.
admin.site.register(Status_lkup)
admin.site.register(Priority_lkup)
admin.site.register(Points_lkup)
admin.site.register(Roles_lkup)
admin.site.register(Sprint)
admin.site.register(Story)
admin.site.register(Task)
admin.site.register(Teammember)
