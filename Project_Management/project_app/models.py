from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone   

class Project(models.Model):
    name =  models.CharField(max_length=100)
    description = models.TextField()
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Admin','Admin'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('project', 'user')

        def __str__(self):
            return f"{self.user.username} - {self.project.name}"

class Task(models.Model):
    STATUS_CHOICES = [
        ('Todo', 'To Do'),
        ('In_progress', 'In_Progress'),
        ('Done', 'Done'),
    ]
    PRIORITY_CHOICE=[
        ('Low','Low'),
        ('Medium','Medium'),
        ('No','No'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Todo') 
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICE, default='No')
    assigned_to = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return {self.user.username} - {self.task.title}
    
