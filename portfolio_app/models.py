from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30, )
    description = models.TextField(max_length=1000)
    project_img = models.ImageField(upload_to='project-img/', blank=True, null=True)
    live_hyperlink = models.URLField(blank=True, null=True)
    
    @property
    def snapshots(self):
        images = self.snapshot_set.all()
        return images

    def __str__(self):
        return self.name


class SnapShot(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='snapshot/')
    description = models.TextField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} from {self.project}'
