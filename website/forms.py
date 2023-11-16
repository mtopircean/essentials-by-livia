from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data