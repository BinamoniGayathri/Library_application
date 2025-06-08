from django import forms
from store.models import store
  

class StoreForm(forms.ModelForm):
    class Meta:
        model=store
        fields="__all__"