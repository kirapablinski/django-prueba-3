from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from enemigosapp.models import Sayayin, Enemigo, Enfrentamientos
from api.serializers import SayayinSerializer, EnemigoSerializer, EnfrentamientosSerializer


# Create your views here.

class SayayinListCreateView(generics.ListCreateAPIView):

    queryset = Sayayin.objects.all()
    serializer_class = SayayinSerializer


class SayayinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Sayayin.objects.all()
    serializer_class = SayayinSerializer

class EnemigoListCreateView(generics.ListCreateAPIView):

    queryset = Enemigo.objects.all()
    serializer_class = EnemigoSerializer


class EnemigoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Enemigo.objects.all()
    serializer_class = EnemigoSerializer

class EnfrentamientoListCreateView(generics.ListCreateAPIView):

    queryset = Enfrentamientos.objects.all()
    serializer_class = EnfrentamientosSerializer


class EnfrentamientoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Enfrentamientos.objects.all()
    serializer_class = EnfrentamientosSerializer

@api_view(['GET'])
def enfrentamientos_por_sayayin(request, sayayin_id):

    try:
        sayayin = Sayayin.objects.get(pk=sayayin_id)
    except Sayayin.DoesNotExist:
        return Response({"error": "Sayayin no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    enfrentamientos = sayayin.enfrentamientos.all()
    serializer = EnfrentamientosSerializer(enfrentamientos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def enfrentamientos_por_enemigo(request, enemigo_id):

    try:
        enemigo = Enemigo.objects.get(pk=enemigo_id)
    except Enemigo.DoesNotExist:
        return Response({"error": "Enemigo no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    enfrentamientos = enemigo.enfrentamientos.all()
    serializer = EnfrentamientosSerializer(enfrentamientos, many=True)
    return Response(serializer.data)