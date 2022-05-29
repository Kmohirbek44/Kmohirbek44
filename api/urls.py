from django.urls import path
from api.views import scrapingrest,scrapingcreate,scrapingchange
urlpatterns=[
    path('api/',scrapingrest.as_view()),
    path('api/create/',scrapingcreate.as_view()),
    path('api/change/<int:pk>/',scrapingchange.as_view())
]