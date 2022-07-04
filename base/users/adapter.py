from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        from allauth.account.utils import user_email, user_field

        data = form.cleaned_data
     
        user_email(user, data.get("email"))
        user_field(user, "name", data.get('name'))
        user_field(user, "id_num", data.get('id_num'))

        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()

        if commit:
            user.save()
        return user
    
    def get_logout_redirect_url(self, request):
        path = "/accounts/login/"
        return path