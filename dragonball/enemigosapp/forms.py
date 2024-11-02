from django import forms
from enemigosapp.models import (Enemigo, Sayayin, Enfrentamientos, )

class FormEnemigo(forms.ModelForm):
    class Meta:
        model = Enemigo
        fields = '__all__'

class FormSayayin(forms.ModelForm):
    class Meta:
        model = Sayayin
        fields = '__all__'

class FormEnfrentamientos(forms.ModelForm):
    class Meta:
        model = Enfrentamientos
        fields = '__all__'