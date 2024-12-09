#urls aparte de la principal
from django.urls import path
from api.views import (
    SayayinListCreateView,
    SayayinRetrieveUpdateDestroyView,
    EnemigoListCreateView,
    EnemigoRetrieveUpdateDestroyView,
    EnfrentamientoListCreateView,
    EnfrentamientoRetrieveUpdateDestroyView,
    enfrentamientos_por_sayayin,
    enfrentamientos_por_enemigo,
)

urlpatterns = [
    # Rutas para Sayayin
    path('sayayines/', SayayinListCreateView.as_view(), name='sayayin-list'),
    path('sayayines/<int:pk>/', SayayinRetrieveUpdateDestroyView.as_view(), name='sayayin-detail'),

    # Rutas para Enemigo
    path('enemigos/', EnemigoListCreateView.as_view(), name='enemigo-list'),
    path('enemigos/<int:pk>/', EnemigoRetrieveUpdateDestroyView.as_view(), name='enemigo-detail'),

    # Rutas para Enfrentamientos
    path('enfrentamientos/', EnfrentamientoListCreateView.as_view(), name='enfrentamiento-list'),
    path('enfrentamientos/<int:pk>/', EnfrentamientoRetrieveUpdateDestroyView.as_view(), name='enfrentamiento-detail'),

    # Rutas personalizadas
    path('sayayin/<int:sayayin_id>/enfrentamientos/', enfrentamientos_por_sayayin, name='enfrentamientos-por-sayayin'),
    path('enemigo/<int:enemigo_id>/enfrentamientos/', enfrentamientos_por_enemigo, name='enfrentamientos-por-enemigo'),
]
