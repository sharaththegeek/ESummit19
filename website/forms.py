from django import forms
from website.models import Admin

class LoginForm(forms.Form):
    userid=forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_userid(self):
        userid=self.cleaned_data.get('userid')
        UObj=Admin.objects.filter(userid=userid)
        if not UObj:
            raise forms.ValidationError("Incorrect ID")
        else:
            return userid
    
    def clean_password(self):
        password=self.cleaned_data.get('password')
        userid=self.cleaned_data.get('userid')
        UObj=Admin.objects.filter(userid=userid)
        if not UObj:
            raise forms.ValidationError("Incorrect ID")
        else:
            UUObj=Admin.objects.get(userid=userid)
            passwd=UUObj.password
            if password==passwd:
               return password
            else:
               raise forms.ValidationError("Incorrect Password")