from django.db import models
from datetime import datetime 
# Create your models here.
class CreateModel(models.Model):
    tittle=models.CharField(max_length=30)
    content=models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True,editable=False,default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    completed=models.BooleanField(default=False)
    acheive=models.BooleanField(default=False)


    def __str__(self):
        return self.tittle
