from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()
users = User.objects.all()

# student ID validations
id_validator = RegexValidator(r'^[0-9A-Z]{2}204[0-9]{3}$', code='wrong')
id_validation_massage = {'wrong':'Sorry ! Your ID is invalid.'}


# allauth form: will show on front-end 
class SignupForm(forms.Form):
    id_num = forms.CharField(max_length=8,strip=True, validators=[id_validator], 
                            error_messages=id_validation_massage,
                            widget=forms.TextInput(
                                attrs={'class' : 'input100',
                                        'placeholder': 'ID'
                                    }))
    name = forms.CharField(max_length=80,
                            widget=forms.TextInput(
                                attrs={'class' : 'input100',
                                        'placeholder': 'Name'
                                    }))

    def clean_id_num(self):
        id_num = self.cleaned_data['id_num']
        if User.objects.filter(id_num=id_num).exists():
            raise forms.ValidationError("This id already exist. Contact admin.")
        return id_num

    class Meta:
        model = User
        fields = ('name', 'id_num', 'email' )

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.id_num = self.cleaned_data['id_num']
        user.save()



# admin-panel form: will show on admin dashboard
class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    id_num = forms.CharField(max_length=8, label='ID', strip=True, validators=[id_validator], error_messages=id_validation_massage)
    class Meta:
        model = User
        fields = ('name', 'id_num', 'email' )

    def clean_id_num(self):
        id_num = self.cleaned_data['id_num']
        if User.objects.filter(id_num=id_num).exists():
            raise forms.ValidationError("This id already exist.")
        return id_num

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()
    id_num = forms.CharField(max_length=8, label='ID', strip=True, validators=[id_validator], error_messages=id_validation_massage)
    class Meta:
        model = User
        fields = ('email', 'password', 'id_num','name', 'is_active', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]