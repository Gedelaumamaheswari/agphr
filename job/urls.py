from django.urls import path
from . import views
app_name='job'
urlpatterns=[
    path("", views.job_list, name='job_list'),
    path("detail/<slug>/", views.job_detail, name='job_detail'),
    path("apply-job/<slug>/", views.apply_job, name='apply_job'),
    path("search/", views.search, name='search'),
    path("skillSearch/", views.skillSearch, name='skillSearch'),
    path("search-result/", views.search_result, name='skillSearch'),
]