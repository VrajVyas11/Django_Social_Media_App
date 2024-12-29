from django import forms

class RegistrationForm(forms.Form):
    firstname = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-[#4CAF50]',
            'placeholder': 'First Name *',
            'autocomplete': 'off',
            'autofocus': 'autofocus',
            'aria-label': 'First Name'
        })
    )
    
    lastname = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-[#4CAF50]',
            'placeholder': 'Last Name *',
            'autocomplete': 'off',
            'aria-label': 'Last Name'
        })
    )

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-[#4CAF50]',
            'placeholder': 'Username *',
            'autocomplete': 'off',
            'aria-label': 'Username'
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-[#4CAF50]',
            'placeholder': 'Email Address *',
            'autocomplete': 'off',
            'aria-label': 'Email Address'
        })
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-[#4CAF50]',
            'placeholder': 'Password *',
            'autocomplete': 'off',
            'aria-label': 'Password'
        })
    )

    confirmation = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-[#4CAF50]',
            'placeholder': 'Confirm Password *',
            'autocomplete': 'off',
            'aria-label': 'Confirm Password'
        })
    )

    profile = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none',
            'accept': 'image/jpeg,image/png,image/webp,image/gif',
            'aria-label': 'Profile Picture'
        })
    )

    cover = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none',
            'accept': 'image/jpeg,image/png,image/webp,image/gif',
            'aria-label': 'Cover Picture'
        })
    )

    def clean_confirmation(self):
        password = self.cleaned_data.get('password')
        confirmation = self.cleaned_data.get('confirmation')
        if password != confirmation:
            raise forms.ValidationError("Password and confirmation do not match.")
        return confirmation



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control inp mb-4 usrnm w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-[#01dd73]',
            'placeholder': 'Username',
            'autocomplete': 'off',
            'autofocus': 'autofocus'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control inp pswd w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-[#01dd73] mb-7',
            'placeholder': 'Password',
            'autocomplete': 'off'
        })
    )