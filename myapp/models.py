from django.db import models

class histobj(models.Model):
    cmd_action = models.CharField(max_length=30)
    cmd_target = models.CharField(max_length=100)
    expre = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)
    remark = models.CharField(max_length=300)
