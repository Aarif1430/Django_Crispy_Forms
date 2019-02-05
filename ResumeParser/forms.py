from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')


class ColorfulContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    summary = forms.CharField(
        label='Summary',
        widget=forms.Textarea(attrs={'placeholder': 'summary'})
    )
    experience = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'experience'})
    )
    city = forms.CharField()
    state = forms.CharField()
    zip_code = forms.CharField(label='Zip')
    projects = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'projects'})
    )
    area_of_interest = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'interests'})
    )
    languages = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'languages'})
    )
    programming_tools = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'software tools'})
    )

    tools_frameworks = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'software tools'})
    )
    community = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'software tools'})
    )
    check_me_out = forms.BooleanField(required=False)
    ''' 
   name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your name here'
            }
        )
    )
    email = forms.EmailField(
        max_length=30,
        widget=forms.TextInput(attrs={'style': 'border-color: green;'})
    )
    job_title = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
        help_text='Write here your message!'
    )

    bio = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
        help_text='Write here your message!'
    )
'''
    