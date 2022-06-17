from django.db import models

# Create your models here.
# 1명 한 test 
class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    feelings_action = models.TextField(max_length=100,null = True)
    tendencies = models.TextField(max_length=100,null = True)
    facial_result = models.TextField(max_length=100,null = True)
    final_result = models.TextField(max_length=100,null = True)

def __str__(self):
        return self.test