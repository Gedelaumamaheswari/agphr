from django.urls import path
from . views import (applicant_analytics_view,
                    applicant_profile_view,
                    )
app_name='applicant'
urlpatterns=[
    path('applicant-analytics/', applicant_analytics_view, name='applicant_analytics'),
    path('applicant-profile/', applicant_profile_view, name='applicant_profile'),
]