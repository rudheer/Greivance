from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms

# Create your models here.
class Complaint(models.Model):
    STATUS =((1,'Closed'),(2, 'Registered'),(3,'Pending'))
    TYPE=(('ClassRoom',"ClassRoom"),('Teacher',"Teacher"),('Security',"Security"),('Health&Hygiene',"Health&Hygiene"),('HostelMess',"HostelMess"),('Academics',"Academics"))
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    Name=models.TextField(max_length=200,blank=False,null=True)
    Branch=models.CharField(blank=False,null=True,max_length=200)
    Course=models.CharField(blank=False,null=True,max_length=200)
    Year=models.CharField(blank=False,null=True,max_length=200)
    Type_of_complaint=models.CharField(choices=TYPE,null=True,max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    DriveLink=models.URLField(max_length=400)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)
    
   
    def __init__(self, *args, **kwargs):
        super(Complaint, self).__init__(*args, **kwargs)
        self.__status = self.status

    def save(self, *args, **kwargs):
        if self.status and not self.__status:
            self.active_from = datetime.now()
        super(Complaint, self).save(*args, **kwargs)
    
    def __str__(self):
     	return self.get_Type_of_complaint_display()
    def __str__(self):
 	    return str(self.user)
