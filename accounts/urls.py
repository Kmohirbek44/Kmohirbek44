from django.urls import path
from .views import login_view, logout_view, delete_user, contact, user_update_view, register_login, choice

app_name='accounts'
urlpatterns=[
    path('login/',login_view,name='login'),
    path('register/',register_login,name='register'),
    path('login_out/',logout_view,name='logout'),
    path('update/', user_update_view, name='update'),
    path('delete/', delete_user, name='delete'),
    path('contact/', contact, name='contact'),
    path('choice/', choice, name='choice'),

]