from django.shortcuts import render
from agphr.utils.decorators import allow_access_to
from users.models import User

@allow_access_to([User.APPLICANT_USER])
def applicant_analytics_view(request,):
  return render(request, 'dashboard/applicant/applicant_analytics.html')
