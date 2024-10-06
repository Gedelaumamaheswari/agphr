from django.urls import path
from .views import (super_admin_analytics_view,
                    super_admin_skill_list_view,
                    super_admin_skill_detail_view,
                    super_admin_update_skill_view,
                    super_admin_delete_skill_view,
                    super_admin_create_skill_view,

                    super_admin_applicant_list_view
                    )

app_name='super_admin'
urlpatterns = [
    path('super-admin-analytics/', super_admin_analytics_view, name='super_admin_analytics'),
    path("super_admin-create-skill/", super_admin_create_skill_view, name='super_admin_create_skill'),
    path("super_admin-skill-list/", super_admin_skill_list_view, name='super_admin_skill_list'),
    path("super_admin-skill-detail/<int:pk>/", super_admin_skill_detail_view, name='super_admin_skill_detail'),
    path("super_admin-update-skill/<int:pk>/", super_admin_update_skill_view, name='super_admin_update_skill'),
    path("super_admin-delete-skill/<int:pk>/", super_admin_delete_skill_view, name='super_admin_delete_skill'),
 
    path("super_admin-applicant-list/", super_admin_applicant_list_view, name='super_admin_applicant_list'),
]
