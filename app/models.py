from django.db import models

# Create your models here.
class Record(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    created_at = models.DateTimeField(auto_now_add = True , null = False)
    first_name = models.CharField(max_length = 100 , null = False )
    last_name = models.CharField(max_length = 100 , null = False) 
    address = models.CharField(max_length = 50 , null = False)
    phone = models.CharField(max_length = 50 , null = False)
    city = models.CharField(max_length = 50 , null = False)
    state = models.CharField(max_length = 50 , null = False)
    email = models.EmailField(max_length = 50 , null = False)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"