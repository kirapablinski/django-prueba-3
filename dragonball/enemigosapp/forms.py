from django import forms
from enemigosapp.models import (Enemigo, Sayayin, Enfrentamientos, )


class FormEnemigo(forms.ModelForm):
    class Meta:
        model = Enemigo
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        
        input_texto = ['nombre', 'raza', 'organizacion']
        for campo in input_texto:
            valor = cleaned_data.get(campo)
            if valor and len(valor) > 50:
                self.add_error(campo, "No puede tener más de 50 caracteres.")

        campos_numericos = ['nivel_de_poder', 'asesinatos', 'veces_que_ha_muerto', 'planetas_destruidos']
        for campo in campos_numericos:
            valor = cleaned_data.get(campo)
            if valor is not None and valor < 0:
                self.add_error(campo, "Ingresa solo números positivos.")

        return cleaned_data

class FormSayayin(forms.ModelForm):
    class Meta:
        model = Sayayin
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        input_texto = ['nombre', 'maestro', 'transformacion_max', 'descripcion_breve']
        
        for input in input_texto:
            valor = cleaned_data.get(input)
            
            if valor:
                if input == 'descripcion_breve' and len(valor) > 100:
                    self.add_error(input, "No puede tener más de 100 caracteres.")
                elif len(valor) > 50:
                    self.add_error(input, "No puede tener más de 50 caracteres.")

        campos_numericos = ['nivel_de_poder', 'veces_ha_resucitado', 'torneos_ganados', 'edad']
        
        for campo in campos_numericos:
            valor = cleaned_data.get(campo)
            if valor < 0:
                self.add_error(campo, "Ingresa solo números positivos.")
        
        return cleaned_data



class FormEnfrentamientos(forms.ModelForm):
    class Meta:
        model = Enfrentamientos
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        
        saga = cleaned_data.get('saga')
        if saga and len(saga) > 50:
            self.add_error('saga', "No puede tener más de 50 caracteres.")
        
        ubicacion = cleaned_data.get('ubicacion')
        if ubicacion and len(ubicacion) > 30:
            self.add_error('ubicacion', "No puede tener más de 30 caracteres.")
        
        return cleaned_data