from django import forms
from .models import Member
from django.core import validators

MEMBERSHIP_CHOICES = [
    ('Swimming', 'Swimming'),
    ('Zumba', 'Zumba'),
    ('Gym', 'Gym'),
    ('Gym&Swimming', 'Gym&Swimming'),
    ('Gym&Sauna', 'Gym&Sauna')
]

PAYMENT_FOR_CHOICES = [
    ('Individual', 'IND'),
    ('Couple', 'COU'),
    ('Family', 'FAM')
]

PAYMENT_TYPE_CHOICES = [
    ('1 Month', '1 Month'),
    ('3 Month', '3 Month'),
    ('6 Month', '6 Month'),
    ('Annual', 'Annual'),
]


class Record(forms.Form):



    ID_number = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":""}))
    date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.SelectDateWidget()
    )
    first_name = forms.CharField(max_length=30,
                    widget=forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={"placeholder":"Last Name"}))
    member_type = forms.CharField(
        max_length=30,
        widget=forms.Select(choices=MEMBERSHIP_CHOICES),
    )
    # payment_for = forms.CharField(
    #     max_length=30,
    #     widget=forms.Select(choices=PAYMENT_FOR_CHOICES),
    # )
    payment_type = forms.CharField(
        max_length=30,
        widget=forms.Select(choices=PAYMENT_TYPE_CHOICES),
    )
    Membership_Start_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.SelectDateWidget()
    )
    Membership_End_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.SelectDateWidget()
    )
    rate = forms.IntegerField()
    paid = forms.IntegerField()
    due = forms.IntegerField()
    Contact_number = forms.CharField(max_length=14)
    Email = forms.EmailField()
    Remarks = forms.CharField(max_length=255)

    def clean(self):
        super(Record, self).clean()

        Contact_number = self.cleaned_data.get('Contact_number')
        ID_number = self.cleaned_data.get('ID_number')
        Email = self.cleaned_data.get('Email')

        if Member.objects.filter(Email = Email).exists():
            self.errors['Email'] = self.error_class(['Email already exists'])

        if Member.objects.filter(ID_number = ID_number).exists():
            self.errors['ID_number'] = self.error_class(['ID already exists'])

        if (len(Contact_number) < 10 or len(Contact_number) > 14) or (not Contact_number.isdigit()):
            self.errors['Contact_number'] = self.error_class(['Invalid Contact number'])

        return self.cleaned_data




# CSStoAddMemberForm
# class PostForm(forms.ModelForm):
# #     class Meta:
#     fields = ['ID_number ', 'date', 'first_name', 'last_name', 'Membership_Start_date ', 
#         'Membership_End_date', 'member_type', 'payment_type', 'rate',
#          'paid' , 'due','Contact_number', 'Email', 'Remarks']    


#         model = Post

#         widgets = {

#         } 