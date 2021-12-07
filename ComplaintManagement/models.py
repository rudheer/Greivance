from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Complaint(models.Model):
    STATUS = ((1, 'Closed'), (2, 'Registered'), (3, 'Pending'))
    TYPE = (('Security', "Security"), ('Health&Hygiene', "Health&Hygiene"), ('HostelMess',
            "HostelMess"), ('Academics', "Academics"), ('Council', "Council"), ('Others', "Others"))
    YEAR = (('1st', "1st"), ('2nd', "2nd"),
            ('3rd', "3rd"), ('4th', "4th"), ('5th', "5th"))
    COURSE = (('B.Tech', "B.Tech"), ('IDD', "IDD"), ('M.Tech', "M.Tech"))
    BRANCH = (('Architecture', "Architecture"), ('Ceramic', "Ceramic"), ('Chemical', "Chemical"), ('Civil', "Civil"), ('Computer Science', "Computer Science"), ('Electrical',
              "Electrical"), ('Electronics', "Electronics"), ('Mechanical', "Mechanical"), ('Metallurgical', "Metallurgical"), ('Mining', "Mining"), ('Pharmaceutical', "Pharmaceutical"))

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Name = models.TextField(max_length=200, blank=False, null=True)
    Branch = models.CharField(choices=BRANCH, null=True, max_length=200)
    Course = models.CharField(choices=COURSE, null=True, max_length=200)
    Year = models.CharField(choices=YEAR, null=True, max_length=200)
    Type_of_complaint = models.CharField(
        choices=TYPE, null=True, max_length=200)
    Description = models.TextField(max_length=4000, blank=False, null=True)
    DriveLink = models.URLField(max_length=400, blank=True)
    Time = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=3)

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
