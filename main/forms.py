from django import forms 
from .models import User , School_Years,Students,Subject,Registration


class SignUp(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    



class Register(forms.Form):
    
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(widget=forms.PasswordInput())
    birthday = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))



class UserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ('user_id','first_name','last_name','username','email','about','is_married','birthday')


class School_yearForm(forms.ModelForm):
    class Meta:
        model = School_Years
        fields = "__all__"



class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
  
