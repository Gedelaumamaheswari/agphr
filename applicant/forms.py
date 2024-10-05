from django import forms
from users.models import User
from applicant.models import Applicant

class ApplicantUserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model=User
        fields = (
            'name',
            'mobile',
        )
class ApplicantForm(forms.ModelForm):
    notice_period = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    linkedin_link = forms.CharField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    qualitative_skills = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3}))
    resume = forms.FileField(widget=forms.widgets.ClearableFileInput(attrs={'class': 'form-control', 'accept':'application/pdf'}))

    class Meta:
        model=Applicant
        fields = (
            'notice_period',
            'linkedin_link',
            'qualitative_skills',
            'subject',
            'message',
            'resume',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].widget.initial_text = "previously uploaded resume"
        self.fields['resume'].widget.input_text = "update your resume(pdf format)"


class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = [
            'user',
            'skills',
            'created_at',
            'updated_at'
        ]

class ApplicantUserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',  # This is still useful for browsers that support it
        }),
        input_formats=['%Y-%m-%d'],  # Accepts yyyy-mm-dd format
    )
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'date_of_birth',
                  'address_line_1',
                  'address_line_2',
                  'city',
                  'state',
                  'country',
                  'postal_code',
                  
        ]