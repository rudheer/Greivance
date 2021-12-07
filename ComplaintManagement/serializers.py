from rest_framework import serializers
from .models import Complaint

class CreateGrievanceSerializer(serializers.Serializer):
    TYPE = (('Security', "Security"), ('Health&Hygiene', "Health&Hygiene"), ('HostelMess',
            "HostelMess"), ('Academics', "Academics"), ('Council', "Council"), ('Others', "Others"))
    YEAR = (('1st', "1st"), ('2nd', "2nd"),
            ('3rd', "3rd"), ('4th', "4th"), ('5th', "5th"))
    COURSE = (('B.Tech', "B.Tech"), ('IDD', "IDD"), ('M.Tech', "M.Tech"))
    BRANCH = (('Architecture', "Architecture"), ('Ceramic', "Ceramic"), ('Chemical', "Chemical"), ('Civil', "Civil"), ('Computer Science', "Computer Science"), ('Electrical',
              "Electrical"), ('Electronics', "Electronics"), ('Mechanical', "Mechanical"), ('Metallurgical', "Metallurgical"), ('Mining', "Mining"), ('Pharmaceutical', "Pharmaceutical"))

    Name = serializers.CharField(max_length=200)
    Branch = serializers.ChoiceField(choices=BRANCH)
    Course = serializers.ChoiceField(choices=COURSE)
    Year = serializers.ChoiceField(choices=YEAR)
    Type_of_complaint = serializers.ChoiceField(choices=TYPE)
    Description = serializers.CharField(max_length=4000)
    DriveLink = serializers.URLField(
        max_length=400, allow_blank=True, required=False)

    def save(self):
        Name = self.validated_data.get('Name')
        Branch = self.validated_data.get('Branch')
        Course = self.validated_data.get('Course')
        Year = self.validated_data.get('Year')
        Type_of_complaint = self.validated_data.get('Type_of_complaint')
        Description = self.validated_data.get('Description')
        DriveLink = self.validated_data.get('DriveLink', '')
        user = self.context["request"].user

        complaint = Complaint.objects.create(
            user=user, Name=Name, Branch=Branch, Course=Course,
            Year=Year, Type_of_complaint=Type_of_complaint,
            Description=Description, DriveLink=DriveLink)
        complaint.save()
        return complaint

class CountGrievanceSerializer(serializers.Serializer):
    def get_count(self):
        user = self.context["request"].user
        user_complaints = Complaint.objects.filter(user=user)
        closed_complaints = user_complaints.filter(status=1)
        registered_complaints = user_complaints.filter(status=2)
        pending_complaints = user_complaints.filter(status=3)

        return {
            "closed": closed_complaints.count(),
            "registered": registered_complaints.count(),
            "pending": pending_complaints.count()
        }

class GrievanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('id', 'Name', 'Branch', 'Year', 'Type_of_complaint',
                  'Description', 'DriveLink', 'status')
