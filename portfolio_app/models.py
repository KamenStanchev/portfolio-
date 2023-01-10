from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30, )
    description = models.TextField(max_length=1000)
    project_img = models.ImageField(upload_to='project-img/', blank=True, null=True)
    live_hyperlink = models.URLField(blank=True, null=True)


class SnapShot(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='snapshot/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
