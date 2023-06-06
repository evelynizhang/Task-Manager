from django.db import models
from django.conf import settings

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )
    due_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    def count_incompleted_tasks(self):
        count = 0
        for task in self.tasks.all():
            if task.is_completed is False:
                count = count + 1
        return count

    def count_completed_tasks(self):
        count = 0
        for task in self.tasks.all():
            if task.is_completed is True:
                count = count + 1
        return count
