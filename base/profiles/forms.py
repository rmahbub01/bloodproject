from django.contrib.auth import get_user_model
from django import forms

from profiles.models import DonorProfile
from profiles.choices import DISTRICT_CHOICES, YEARS_CHOICE, BLOOD_GROUP

User = get_user_model()


class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=80,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'your name'
                                      }))

    class Meta:
        model = User
        fields = ("name",)


class DonorProfileForm(forms.ModelForm):
    contact_email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'example@mail.com'
                   }))

    contact_number = forms.CharField(max_length=11,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control',
                                                'placeholder': '019xxxxxxxxx'
                                                }), required=False)
    bio = forms.CharField(max_length=300,
                          widget=forms.TextInput(
                              attrs={'class': 'form-control',
                                     'placeholder': 'something about you'
                                     }), required=False)
    hobbies = forms.CharField(max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control',
                                         'placeholder': 'Playing, Gaming (seperate with commas)'
                                         }), required=False)
    department = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'job title'
               }), required=False)
    job_title = forms.CharField(max_length=60,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'job title'
                                           }), required=False)
    job_location = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control',
                                              'placeholder': 'job location'
                                              }), required=False)
    city = forms.ChoiceField(choices=DISTRICT_CHOICES, widget=forms.Select(attrs={'class':'form-select form-select-lg mb-3'}))
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP, widget=forms.Select(attrs={'class':'form-select form-select-lg mb-3'}))


    fb_profile_link = forms.CharField(max_length=150, required=False)
    whatsapp_number = forms.CharField(max_length=11, required=False)

    class Meta:
        model = DonorProfile
        fields = ("dp", "blood_group", "contact_email", "contact_number", "city", "bio", "fb_profile_link", "whatsapp_number",
                  "department", "year", "hobbies", "current_status",
                  "job_title", "job_location")


# TODO:
 # add model for this form
 # add fields
 # add to view
class BloodStatusForm(forms.ModelForm):

    class Meta:
        model = ''
        fields = ("",)
