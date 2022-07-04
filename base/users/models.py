import uuid

from django.contrib.auth import password_validation
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from django.db import models

from .managers import UserManager

# student validations
id_validator = RegexValidator(r'^[0-9]{2}[1-9]0[0-9][0-9]{3}$', code='wrong')
id_validation_massage = {'wrong':'sorry you may not a student or teacher of the department.'}

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('email', unique=True)
    name = models.CharField(max_length=150, blank=False)
    id_num = models.CharField(max_length=8, validators=[id_validator], error_messages=id_validation_massage)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_site_admin = models.BooleanField(default=False)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = False

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)
        
        if self._password is not None:
            password_validation.password_changed(self._password, self)
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
