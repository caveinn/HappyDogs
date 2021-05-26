from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from .models import Dog

class DogCreateForm(forms.ModelForm):
    """
    Signup form class
    """


    first_name = forms.CharField(
        label='First Name', widget=forms.TextInput(attrs={'placeholder': 'John'}))
    last_name = forms.CharField(
        label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Doe'}))

    class Meta:
        model = Dog
        fields = ('first_name', 'last_name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('submit', 'Add'))
