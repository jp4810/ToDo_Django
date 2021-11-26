from django.db import models

class Tasks(models.Model):
    class Meta:
        db_table = 'tasks'
    title = models.TextField(
        null=False
    )
    state = models.BooleanField(
        null=False,
        default=False
    )
    description = models.TextField(
        default=""
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
