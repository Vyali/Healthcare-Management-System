from django import forms


class userRegisterForm(forms.Form):
    user_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs ={'class' : 'form-control'}))
    re_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
class userDetailForm(forms.Form):
    first_name=forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'first name'}))
    middle_name=forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder': ' middle name'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'last name'}))
    dob = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Date of birth'}))
    phone_number = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Contact Number'}))
    address = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'address'}))
    height = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Height'}))
    weight = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Weight'}))
    med_insurance_provider = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Provider'}))
    med_insurance_policy_no = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Policy number'}))
    emergency_contact = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'emergency contact'}))

    blood_group = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'blood group' }))

class userLoginForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
