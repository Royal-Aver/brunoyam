from django.urls import path

from .views import main_page, UsersRegistration

urlpatterns = [
    path('', main_page, name='index'),
    path('add/', UsersRegistration.as_view(), name='add')
]