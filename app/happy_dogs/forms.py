from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from .models import Dog, BoardingVisit

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

class BoardingVisitForm(forms.ModelForm):
    """
    Signup form class
    """
    # dog = forms.ModelChoiceField(queryset=Dog.objects.all(), label="Dog")
    start_date = forms.DateField(
        label='Start Date', widget=forms.SelectDateWidget())
    end_date = forms.DateField(
        label='End Date', widget=forms.SelectDateWidget())

    class Meta:
        model = BoardingVisit
        fields = ('start_date', 'end_date','dog' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        # self.helper.add_input(Submit('submit', 'Add'))

    def clean(self):
        super().clean()
        form_data = self.cleaned_data
        dog = form_data['dog']
        start_date = form_data['start_date']
        end_date = form_data['end_date']
        start_date_overlaps = dog.boardingvisit_set.filter(start_date__range=[start_date, end_date] ).exists()
        end_date_overlaps = dog.boardingvisit_set.filter(end_date__range=[start_date, end_date] ).exists()

        if end_date_overlaps or start_date_overlaps:
            self.add_error(None, 'The dates overlap with another visit')

        return form_data

class QueryDatesForm(forms.Form):
    """
    Signup form class
    """
    # dog = forms.ModelChoiceField(queryset=Dog.objects.all(), label="Dog")
    start_date = forms.DateField(
        label='Start Date', widget=forms.SelectDateWidget())
    end_date = forms.DateField(
        label='End Date', widget=forms.SelectDateWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        # self.helper.add_input(Submit('submit', 'Add'))
