from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField('使用者名稱', max_length=20)
    subject = models.CharField('內容主旨', max_length=50)
    content = models.TextField('內容')
    time = models.DateTimeField('', auto_now_add=True)

    def __str__(self):
        return self.user + ':' + self.subject