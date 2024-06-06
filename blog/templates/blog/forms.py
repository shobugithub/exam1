from django import forms # type: ignore

class UserSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255, required=False)
