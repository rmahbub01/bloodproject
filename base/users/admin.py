from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    readonly_fields = ("date_joined", 'updated')
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal info', {'fields': ('name', 'id_num', 'date_joined')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'id_num', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'id_num')
    list_filter = ('date_joined',)
    search_fields = ('email', 'id_num', 'is_active', 'is_superuser',)
    ordering = ('date_joined',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)