from django import forms
from .models import GeeksModel

# declare a new form with a name "GeeksModel"

# creating a form
class GeeksForm(forms.ModelForm):

    # create meta class
    class Meta :
        # specify model to be used
        model = GeeksModel

        # specify fileds to be used
        fields = [
            "title",
            "description",
        ]
