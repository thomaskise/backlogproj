from django.test import TestCase
from .models import Status_lkup, Priority_lkup, Points_lkup, Roles_lkup, Story, Task, Teammember, Sprint
from .views import index, getbacklog, getstorydetails, newtask, newstory
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import StoryForm, TaskForm
import datetime

# Test Models
class StoryTest(TestCase):
    def test_string(self):              #must start with test - following is whatever
        title=Story(
            storytitle="Developer needs task view"
        )                               #local, not in db
        self.assertEqual(
            str(title), 
            title.storytitle
        )                               #note str(type) - pass instance of class, not class

    def test_table(self):
        self.assertEqual(str(Story._meta.db_table), 'story')

class TaskTest(TestCase):
    def test_string(
            self
        ):                              #must start with test - following is whatever
        title=Task(
            tasktitle="Create Taskview Assets"
        )                               #local, not in db
        self.assertEqual(
            str(title),
            title.tasktitle
        )                           #note str(type) - pass instance of class, not class

    def test_table(self):
        self.assertEqual(
            str(Task._meta.db_table),
            'task'
        )

class SprintTest(TestCase):
    def test_string(
            self
        ):                              #must start with test - following is whatever
        sprint=Sprint(
            sprintlabel="Sprint 1"
        )                               #local, not in db
        self.assertEqual(
            str(sprint),
            sprint.sprintlabel
        )                           #note str(type) - pass instance of class, not class

    def test_table(self):
        self.assertEqual(
            str(Sprint._meta.db_table),
            'sprint'
        )

# Test Views (direct)
class BacklogTest(TestCase):    
    def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('backlog'))
       self.assertEqual(response.status_code, 200)

# Test Views (with ID)
class GetStoryDetailsTest(TestCase):
    def setUp(self):
        self.teamrole1=Roles_lkup.objects.create(
            rolename='Product Manager', 
            rolenamesort=3
        )
        self.teamrole2=Roles_lkup.objects.create(
            rolename='Product Owner', 
            rolenamesort=4
        )
        self.priority=Priority_lkup.objects.create(
            storypriority='must',
            storyprioritysort=1
        )
        self.status=Status_lkup.objects.create(
            storystatus='In Sprint',
            storystatussort=1
        )
        self.points=Points_lkup.objects.create(
            storypoint=5
        )
        self.sprint=Sprint.objects.create(
            sprintlabel='Sprint 1'
        )
        self.bizowner=Teammember.objects.create(
            firstname='Bill',
            lastname='Newman',
            teammemberrole=self.teamrole1
        )
        self.techowner=Teammember.objects.create(
            firstname='Thom',
            lastname='Harrington',
            teammemberrole=self.teamrole2
        )
        self.story=Story.objects.create(
            storytitle='Employeer needs to post Gigs',
            storydetail='As an employeer I need to post Gigs so I can fill my positions', 
            storyenterdate='2019-04-02', 
            storyclosedate='2019-06-02', 
            storypriority=self.priority, 
            storystatus=self.status, 
            storyeffortpoints=self.points, 
            assignedsprint=self.sprint, 
            ownerproduct=self.bizowner, 
            ownersprintteam=self.techowner            
        )

    def test_story_detail_success(self):
        response=self.client.get(
            reverse(
                'storydetails', args=(self.story.id,)
            )
        )

# Test Forms
class FormTest(TestCase):

    def setUp(self):
        self.user=User.objects.create(
            username='user1',
            password='P@ssw0rd1'
        )
        self.priority=Priority_lkup.objects.create(
            storypriority='must',
            storyprioritysort=1
        )
        self.status=Status_lkup.objects.create(
            storystatus='In Sprint',
            storystatussort=1
        )
        self.points=Points_lkup.objects.create(
            storypoint=5
        )
        self.sprint=Sprint.objects.create(
            sprintlabel='Sprint 1'
        )
        self.teamrole1=Roles_lkup.objects.create(
            rolename='Product Manager', 
            rolenamesort=3
        )
        self.bizowner=Teammember.objects.create(
            firstname='Bill',
            lastname='Newman',
            teammemberrole=self.teamrole1
        )
        self.teamrole2=Roles_lkup.objects.create(
            rolename='Product Owner', 
            rolenamesort=4
        )
        self.techowner=Teammember.objects.create(
            firstname='Thom',
            lastname='Harrington',
            teammemberrole=self.teamrole2
        )
        self.teamrole3=Roles_lkup.objects.create(
            rolename='Scrum Master', 
            rolenamesort=5
        )
        self.taskowner=Teammember.objects.create(
            firstname='James',
            lastname='Papa Sado',
            teammemberrole=self.teamrole3
        )
        self.story=Story.objects.create(
            storytitle='Employeer needs to post Gigs',
            storydetail='As an employeer I need to post Gigs so I can fill my positions', 
            storyenterdate='2019-04-02', 
            storyclosedate='2019-06-02',
            storypriority=self.priority, 
            storystatus=self.status, 
            storyeffortpoints=self.points, 
            assignedsprint=self.sprint,
            ownerproduct=self.bizowner,
            ownersprintteam=self.techowner            
        )
    
    def test_newtaskform(self):
        data={
            'tasktitle'         : 'Create database field',
            'story'             : self.story,
            'teammembermember'  : self.taskowner,
            'taskdetails'       : 'Write SQL script, initial db ...',
            'taskefforttime'    : 8.5

        }
        form=TaskForm(data=data)
        self.assertTrue(form.is_valid)

# Test Authentication
class New_Story_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(
            username='testuser1',
            password='P@ssw0rd1'
        )
        self.priority=Priority_lkup.objects.create(
            storypriority='must',
            storyprioritysort=1
        )
        self.status=Status_lkup.objects.create(
            storystatus='In Sprint',
            storystatussort=1
        )
        self.points=Points_lkup.objects.create(
            storypoint=5
        )
        self.sprint=Sprint.objects.create(
            sprintlabel='Sprint 1'
        )
        self.teamrole1=Roles_lkup.objects.create(
            rolename='Product Manager', 
            rolenamesort=3
        )
        self.bizowner=Teammember.objects.create(
            firstname='Bill',
            lastname='Newman',
            teammemberrole=self.teamrole1
        )
        self.teamrole2=Roles_lkup.objects.create(
            rolename='Product Owner', 
            rolenamesort=4
        )
        self.techowner=Teammember.objects.create(
            firstname='Thom',
            lastname='Harrington',
            teammemberrole=self.teamrole2
        )
        self.teamrole3=Roles_lkup.objects.create(
            rolename='Scrum Master', 
            rolenamesort=5
        )
        self.taskowner=Teammember.objects.create(
            firstname='James',
            lastname='Papa Sado',
            teammemberrole=self.teamrole3
        )
        self.story=Story.objects.create(
            storytitle='Employeer needs to post Gigs',
            storydetail='As an employeer I need to post Gigs so I can fill my positions', 
            storyenterdate='2019-04-02', 
            # storyclosedate='2019-06-02', #optional field can be on or off
            storypriority=self.priority, 
            storystatus=self.status, 
            storyeffortpoints=self.points, 
            assignedsprint=self.sprint,
            ownerproduct=self.bizowner,
            ownersprintteam=self.techowner            
        )        
        self.task=Task.objects.create(
            tasktitle='Create database field',
            story=self.story
        )
        self.task.Teammembermember.add(
            self.taskowner
        )

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(
            reverse('newstory')
        )
        self.assertRedirects(
            response,
            '/accounts/login/?next=/sprintapp/newstory/'
        )

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(
            username='testuser1', 
            password='P@ssw0rd1'
        )
        response=self.client.get(
            reverse('newtask')
        )
        self.assertEqual(
            str(response.context['user']),
            'testuser1'
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response, 
            'sprintapp/newtask.html'
        )