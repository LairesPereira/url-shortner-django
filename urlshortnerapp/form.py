from django import forms

class ShortnerForm(forms.Form):
   urlToShort = forms.CharField(
                        label='', 
                        max_length=255, 
                        widget=forms.TextInput(
                           attrs = {
                              'placeholder': 'Cole sua URL aqui',
                              'class': 'subscribe_form form-control'
                           }
                        ))
