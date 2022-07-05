from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

from django_resized import ResizedImageField

from .choices import (
    BLOOD_GROUP,
    YEARS_CHOICE,
    STATUS_CHOICE,
    DISTRICT_CHOICES,
)


User = get_user_model()
YEARS_CHOICE_P = YEARS_CHOICE.copy()
YEARS_CHOICE_P.append(("grad", "Graduated"))

# validation
id_validator = RegexValidator(r"^[0-9A-Z]{2}204[0-9]{3}$", code="wrong")
comma_aphabets = RegexValidator(
    r"^[, a-zA-Z]*$", "Separate with comma.", code="invalid"
)


class Profile(models.Model):
    dp = ResizedImageField(
        size=[200, 200],
        crop=["middle", "center"],
        quality=75,
        keep_meta=False,
        verbose_name="profile picture",
        upload_to="profileImages",
        force_format="JPEG",
        default="profileImages/avater.jpeg",
    )
    contact_email = models.EmailField(verbose_name="contact_mail")
    contact_number = models.CharField(max_length=11)
    city = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    blood_group = models.CharField(max_length=8, choices=BLOOD_GROUP)
    bio = models.CharField(max_length=300, blank=True, null=True)
    fb_profile_link = models.CharField(max_length=150, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=11, blank=True, null=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    
    last_donated = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

class DonorProfile(Profile):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="donor_profile", editable=False
    )
    year = models.CharField(max_length=5, choices=YEARS_CHOICE_P)
    hobbies = models.CharField(max_length=100, blank=True, validators=[comma_aphabets], null=True)
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    job_title = models.CharField(max_length=60, blank=True, null=True)
    job_location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "profile(donor)"
        verbose_name = "profiles(donor)"

    def __str__(self):
        return f"{self.user.id_num} ==> {self.user.name}"

    def save(self, *args, **kwargs):
        if self.hobbies:
            self.hobbies = ", ".join(
                [hobby.strip() for hobby in self.hobbies.strip().split(",")]
            )

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.dp.delete()

        return super().delete(*args, **kwargs)

    @property
    def get_hobbies_as_list(self):
        return self.hobbies.split(",")
    