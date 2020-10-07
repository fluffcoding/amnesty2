from django.urls import path

from .views import main_dashboard

app_name = 'team'

urlpatterns = [
    path('', main_dashboard, name='dashboard')
]