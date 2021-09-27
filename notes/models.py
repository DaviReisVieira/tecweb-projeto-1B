from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{0}. {1}'.format(self.id,self.name)

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return '{}. {}'.format(self.id,self.title)
