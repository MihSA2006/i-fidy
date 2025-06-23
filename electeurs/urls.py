from django.urls import path
from .views import ArrondissementListCreate, ArrondissementRetrieveUpdateDestroy, ElecteurListCreate, ElecteurRetrieveUpdateDestroy


urlpatterns = [
    # Arrondissement endpoints
    path('arrondissements/', ArrondissementListCreate.as_view(), name='arrondissement-list-create'),
    path('arrondissements/<int:pk>/', ArrondissementRetrieveUpdateDestroy.as_view(), name='arrondissement-retrieve-update-destroy'),
    
    # Electeur endpoints
    path('electeurs/', ElecteurListCreate.as_view(), name='electeur-list-create'),
    path('electeurs/<int:pk>/', ElecteurRetrieveUpdateDestroy.as_view(), name='electeur-retrieve-update-destroy'),
]