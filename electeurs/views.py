from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Electeur, Arrondissement
from .serializers import ElecteurSerializer, ArrondissementSerializer

class ArrondissementListCreate(ListCreateAPIView):
    queryset = Arrondissement.objects.all()
    serializer_class = ArrondissementSerializer

class ArrondissementRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Arrondissement.objects.all()
    serializer_class = ArrondissementSerializer

class ElecteurListCreate(ListCreateAPIView):
    queryset = Electeur.objects.all()
    serializer_class = ElecteurSerializer

class ElecteurRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Electeur.objects.all()
    serializer_class = ElecteurSerializer