from rest_framework.generics import ListAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from scraping.models import Vakation
from .serialazers import scraprest
class scrapingrest(ListAPIView):
    queryset = Vakation.objects.all()
    serializer_class = scraprest

class scrapingcreate(ListCreateAPIView):
    queryset = Vakation.objects.all()
    serializer_class = scraprest

class scrapingchange(RetrieveUpdateDestroyAPIView):
    queryset = Vakation.objects.all()
    serializer_class = scraprest

