from django.db import models

# Create your models here.
from django.utils import timezone

# Create your models here.
class User(models.Model):
    User_id = models.AutoField(primary_key = True)
    Full_name = models.TextField(max_length = 100)
    Image = models.FileField(upload_to='images/', null=True)
    Email = models.EmailField(max_length = 50, null=True)
    Address = models.TextField(max_length = 200, null = True)
    Age = models.IntegerField(null = True)
    Phone_Number = models.TextField(max_length=10, null = True)
    Password = models.TextField(max_length = 15, null = True)
    Date_Time = models.DateTimeField(auto_now = True, null = True)
    User_Status = models.TextField(default = 'pending', max_length=50, null = True)
    Otp_Num = models.IntegerField(null = True)
    Otp_Status = models.TextField(default = 'pending', max_length = 60, null = True)
    Last_Login_Time = models.TimeField(auto_now_add=True,null = True)
    Last_Login_Date = models.DateField(auto_now_add=True,null = True)
    No_Of_Times_Login = models.IntegerField(default = 0, null = True)
    Message =models.TextField(max_length=250,null=True)
    
    class Meta:
        db_table = 'user'
        
class Last_login(models.Model):
    Id = models.AutoField(primary_key = True)
    Login_Time = models.DateTimeField(auto_now = True, null = True)

    class Meta:
        db_table = "last_login"