from rest_framework import serializers
from enemigosapp.models import Enemigo, Sayayin, Enfrentamientos


class EnemigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemigo
        fields = '__all__'

    def validate(self, data):
        # Validación para campos de texto
        input_texto = ['nombre', 'raza', 'organizacion']
        for campo in input_texto:
            valor = data.get(campo)
            if valor and len(valor) > 50:
                raise serializers.ValidationError({campo: "No se puede tener más de 50 caracteres."})

        # Validación para campos numéricos
        campos_numericos = ['nivel_de_poder', 'asesinatos', 'veces_que_ha_muerto', 'planetas_destruidos']
        for campo in campos_numericos:
            valor = data.get(campo)
            if valor is not None and valor < 0:
                raise serializers.ValidationError({campo: "Ingresa solo números positivos."})

        return data #copia y pega del form modificado para que funcione con serializer


class SayayinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sayayin
        fields = '__all__'

    def validate(self, data):
        # Validación para campos de texto
        input_texto = ['nombre', 'maestro', 'transformacion_max', 'descripcion_breve']
        for campo in input_texto:
            valor = data.get(campo)
            if valor:
                if campo == 'descripcion_breve' and len(valor) > 100:
                    raise serializers.ValidationError({campo: "No puede tener más de 100 caracteres."})
                elif len(valor) > 50:
                    raise serializers.ValidationError({campo: "No puede tener más de 50 caracteres."})

        # Validación para campos numéricos
        campos_numericos = ['nivel_de_poder', 'veces_ha_resucitado', 'torneos_ganados', 'edad']
        for campo in campos_numericos:
            valor = data.get(campo)
            if valor is not None and valor < 0:
                raise serializers.ValidationError({campo: "Solo puede tener números positivos."})

        return data


class EnfrentamientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfrentamientos
        fields = '__all__'

    def validate(self, data):
        # Validación para saga
        saga = data.get('saga')
        if saga and len(saga) > 50:
            raise serializers.ValidationError({'saga': "No puede tener más de 50 caracteres."})

        # Validación para ubicación
        ubicacion = data.get('ubicacion')
        if ubicacion and len(ubicacion) > 30:
            raise serializers.ValidationError({'ubicacion': "No puede tener más de 30 caracteres."})

        return data
