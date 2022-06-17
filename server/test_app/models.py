from django.db import models

# Create your models here.
# 1명 한 test 
class Test(models.Model):
    feelings_action = models.TextField(max_length=120,null = True)
    tendencies = models.TextField(max_length=40,null = True)
    facial_result = models.TextField(max_length=50,null = True)
    final_result = models.TextField(max_length=120,null = True)


    def __str__(self):
        return self.test
        

