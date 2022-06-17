from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# 1명 한 test
class BigData(models.Model):
    tendencies = models.TextField(max_length=100,null = True)
    final_result = models.TextField(max_length=100,null = True)

class AI(models.Model):
    feelings_action = models.TextField(max_length=100,null = True)
    facial_result = models.TextField(max_length=100,null = True)
    final_result = models.TextField(max_length=100,null = True)

def __str__(self):
        return self.Mzroad