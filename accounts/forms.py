from django import forms
from .models import Account, UserProfile, BillingAddress, Country, State, City
import re

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class': 'form-control',}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
        self.fields['email'].widget.attrs['placeholder']='Enter Email Address'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter Phone Number'

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        phone_number = self.cleaned_data.get('phone_number')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if not first_name.isalpha():
            raise forms.ValidationError("First name should contain only letters!")

        if not last_name.isalpha():
            raise forms.ValidationError("Last name should contain only letters!")
        
        if not re.match(r'^\d{10}$', phone_number):
            raise forms.ValidationError("Phone number must be in a valid format (10 digits).")
        
        if password != confirm_password:
            raise forms.ValidationError("Password does not match!")
        
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            raise forms.ValidationError("Password should be at least 8 characters and contain a combination of uppercase, lowercase, digits, and special symbols!")
        
        
        

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        phone_number = self.cleaned_data.get('phone_number')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if not first_name.isalpha():
            raise forms.ValidationError("First name should contain only letters!")

        if not last_name.isalpha():
            raise forms.ValidationError("Last name should contain only letters!")
        
        if not re.match(r'^\d{10}$', phone_number):
            raise forms.ValidationError("Phone number must be in a valid format (10 digits).")


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ('first_name', 'last_name', 'phone_number', 'address_line_1', 'address_line_2', 'city', 'state', 'country')
        widgets = {
            'address_line_1': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }

    def __init__(self, *args, **kwargs):
        super(BillingAddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        # Adjust foreign key fields
        self.fields['country'].queryset = Country.objects.all()
        self.fields['state'].queryset = State.objects.none()  # Initially no states
        self.fields['city'].queryset = City.objects.none()    # Initially no cities

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country_id=country_id)
            except (ValueError, TypeError):
                pass
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id)
            except (ValueError, TypeError):
                pass

    def clean(self):
        cleaned_data = super(BillingAddressForm, self).clean()
        phone_number = self.cleaned_data.get('phone_number')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if not first_name.isalpha():
            raise forms.ValidationError("First name should contain only letters!")

        if not last_name.isalpha():
            raise forms.ValidationError("Last name should contain only letters!")
        
        if not re.match(r'^\d{10}$', phone_number):
            raise forms.ValidationError("Phone number must be in a valid format (10 digits).")