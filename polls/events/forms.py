from django import forms
from .models import Question, Choice

class choices(forms.Form):
    
    choice = forms.MultipleChoiceField(choices=Choice.objects.values_list("id", "choice_text"),
                                        widget=forms.CheckboxSelectMultiple(),
                                        label='Vote')