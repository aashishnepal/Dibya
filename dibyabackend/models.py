from django.db import models

class Member(models.Model):
    ID_number = models.CharField(max_length = 20, null = False)
    date = models.DateField()
    first_name = models.CharField(max_length = 30, null = False)
    last_name = models.CharField(max_length=30, null=False)
    Membership_Start_date = models.DateField()
    Membership_End_date = models.DateField()
    member_type = models.CharField(max_length=50, null=False)
    payment_type = models.CharField(max_length=10, null=False)
    rate = models.IntegerField(null = False)
    paid = models.IntegerField(null = False)
    due = models.IntegerField(null = False)
    Contact_number = models.CharField(max_length = 14, null = False)
    Email = models.EmailField(null = False)
    Remarks = models.CharField(max_length = 255)

    def __str__(self):
        return self.ID_number + "  " + self.first_name + " " + self.last_name
