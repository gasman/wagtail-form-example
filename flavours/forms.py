from django import forms

from flavours.models import IceCreamFlavour


class FlavourSuggestionForm(forms.ModelForm):
    """
    A form for suggesting an ice cream flavour. Here we're using a Django ModelForm, but this could
    be as simple or as complex as you like -
    see https://docs.djangoproject.com/en/1.9/topics/forms/
    """
    class Meta:
        model = IceCreamFlavour
        fields = ['flavour_name', 'your_name']
