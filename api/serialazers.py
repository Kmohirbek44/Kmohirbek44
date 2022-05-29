from rest_framework import serializers
from scraping.models import Vakation

class scraprest(serializers.ModelSerializer):
    class Meta:
        model=Vakation
        fields=('title','company','description','city','language','timestap')