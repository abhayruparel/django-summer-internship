# from .models import JobApplication
# from django import forms


# class JobApplicationForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(JobApplicationForm, self).__init__(*args, **kwargs)
#         self.fields['fname'].label = "First Name"
#         self.fields['lname'].label = "Last Name"

#     class Meta:
#         model = JobApplication
#         fields = '__all__'
#         widgets = {
#             'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
#             'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             # 'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'zip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'relation_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'dob': forms.DateInput(attrs={'class': 'form-control'}),
#             'date_created': forms.DateTimeInput(attrs={'class': 'form-control'}),

#         }
