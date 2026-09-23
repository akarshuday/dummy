from django import forms

from autos.models import Make


class MakeForm(forms.ModelForm):
    class Meta:
        model = Make
        fields = '__all__'