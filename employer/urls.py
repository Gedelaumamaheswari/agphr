from django.urls import path
from . import views

app_name='employer'
urlpatterns=[
    path('employer-analytics/', views.employer_analytics_view, name='employer_analytics'),
    path('employer-job-list/', views.employer_job_list_view, name='employer_job_list'),
    path("employer-job-detail/<slug>/", views.employer_job_detail_view, name='employer_job_detail'),
    path('employer-profile/', views.employer_profile_view, name='employer_profile'),
    path("employer-create-job/", views.employer_create_job_view, name='employer_create_job'),
    path("employer-job-list/", views.employer_job_list_view, name='employer_job_list_view'),
    path("employer-update-job/<slug>/", views.employer_job_update_view, name='employer_update_job'),
    path("employer-delete-job/<slug>/", views.employer_job_delete_view, name='employer_delete_job'),
    path("employer-publish-job/<slug>/", views.employer_job_publish_view, name='employer_publish_job'),
    path("employer-unpublish-job/<slug>/", views.employer_job_unpublish_view, name='employer_unpublish_job'),

    path("employer-applicant-list/", views.employer_applicant_list_view, name='employer_applicant_list'),
    path("employer-export-applicant-list/", views.employer_export_applicant_list_view, name='employer_export_applicant_list'),
    path("employer-toggle-recommended-jobs/<slug>/", views.employer_toggle_recommended_jobs_view, name='employer_toggle_recommended_jobs'),
]