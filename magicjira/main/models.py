from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=500)
    key = models.CharField(max_length=500)
    lead = models.CharField(max_length=500)
    category = models.CharField(max_length=500)

class Tag(models.Model):
    name = models.CharField(max_length=500)
    label = models.CharField(max_length=500)

class Issue(models.Model):
    Project = models.ForeignKey(Project, on_delete = models.CASCADE)
    state = models.CharField(max_length=500)
    assignee = models.ForeignKey(User, on_delete = models.CASCADE, related_name="assigned_issues")
    summary = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    # comment = models.CharField(max_length=500)
    key = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag)
    type = models.CharField(max_length=500)
    reporter = models.ForeignKey(User, on_delete = models.CASCADE, related_name="reported_issues")
    # attachment = models.CharField(max_length=500)
    solution = models.TextField()
    watchers = models.ManyToManyField(User)
    priority = models.CharField(max_length=500)

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField()

class Attachment(models.Model):
    date_uploaded = models.DateTimeField()
    file = models.FileField()




    

