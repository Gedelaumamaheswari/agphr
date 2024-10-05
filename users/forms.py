from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    contact = forms.CharField(
        label='Mobile Number',
        help_text='Enter a valid 10-digit mobile number',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
        required=True,
    )

    user_type = forms.ChoiceField(
        choices=[
            ('', 'Select your user type'),
            (User.EMPLOYER, 'Employer'),
            (User.APPLICANT_USER, 'Applicant')
        ],
        label='User Type',
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
        help_text='Please select the type of user you are.'
    )

    class Meta:
        model = User
        fields = ['user_type', 'contact', 'password1', 'password2']

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')

        # Regex patterns for validation
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        mobile_pattern = r'^\d{10}$'

        if re.match(email_pattern, contact):
            if User.objects.filter(email=contact).exists():
                raise forms.ValidationError("An account with this email address already exists.")
            self.cleaned_data['email'] = contact 
        elif re.match(mobile_pattern, contact):
            if User.objects.filter(mobile=contact).exists():
                raise forms.ValidationError("An account with this mobile number already exists.")
            self.cleaned_data['mobile'] = contact
        else:
            raise forms.ValidationError("Please enter a valid email address or a 10-digit mobile number.")
        
        return contact


class OTPVerificationForm(forms.Form):
    otp_code = forms.CharField(
        max_length=6,
        label='OTP Code',
        widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'})
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your mobile number'}),
        label='Mobile',
        help_text='Please enter the mobile number you used to register.'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        label='Password',
        help_text='Enter the password you created during registration.'
    )
