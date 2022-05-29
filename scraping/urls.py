from django.urls import path, include

from .views import scraping_home, L_List, resume_edit, resume, resume_list, resume_home, GeneratePdf

app_name = 'scraping'

urlpatterns = [
    path('', L_List.as_view(), name='home'),
    path('api/',include('api.urls')),
    path('page/<int:page>/',scraping_home,name='page'),
    # path('detail/<int:pk>/',L_List.as_view())
    path('resume/', resume, name='resume'),
    path('resume_search/', resume, name='resume_search'),
    path('resume_edit/', resume_edit, name='resume_edit'),
    path('resume_home', resume_list.as_view(), name='resume_list'),
    path('page/<int:page>/',resume_home,name='resume_home'),
    path('pdf/',GeneratePdf.as_view()),

]
