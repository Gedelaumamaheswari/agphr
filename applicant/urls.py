from django.urls import path
from . import views

app_name='applicant'
urlpatterns=[
    path('applicant-analytics/', views.applicant_analytics_view, name='applicant_analytics'),
]