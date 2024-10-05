from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from agphr.utils.decorators import allow_access_to
from users.models import User
from job.forms import  AddSkill
from job.models import Skill

@allow_access_to([User.SUPER_ADMIN])
def super_admin_analytics_view(request):
  return render(request, 'dashboard/super_admin/super_admin_analytics.html')

@allow_access_to([User.SUPER_ADMIN])
def super_admin_user_list_view(request):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_user_detail_view(request, pk):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_employeer_list_view(request):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_employeer_detail_view(request, slug):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_applicant_list_view(request):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_applicant_detail_view(request):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_job_list_view(request):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_job_detail_view(request, slug):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_create_skill_view(request):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_skill_list_view(request):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_skill_detail_view(request, pk):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_skill_update_view(request, pk):
    pass

@allow_access_to([User.SUPER_ADMIN])
def super_admin_skill_delete_view(request, pk):
    pass


@allow_access_to([User.SUPER_ADMIN])
def super_admin_create_skill_view(request):
    if request.method == "POST":
        form = AddSkill(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill added successfully")
    form = AddSkill()
    return render(request, 'dashboard/super_admin/super_admin_create_skill.html', {'form':form})

@method_decorator(allow_access_to([User.SUPER_ADMIN]), name="dispatch")
class EmployerSkillListView(ListView):
    model = Skill
    template_name = 'dashboard/super_admin/super_admin_skill_list.html'
    context_object_name = 'skills'
    
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('name')
        sorting_value = self.request.GET.get('sorting_value')
        skills = Skill.objects.skill_lists(query, sorting_value)
        if query is not None:
            skills_length = len(skills)
            messages.success(self.request, f"{skills_length if skills_length >=1  else 'No'} job found for {query}.")
        return skills
super_admin_skill_list_view = EmployerSkillListView.as_view()

@allow_access_to([User.SUPER_ADMIN])
def super_admin_skill_detail_view(request, pk):
    skill = Skill.objects.skill_detail(pk)
    return render(request, 'dashboard/super_admin/super_admin_skill_detail.html', {'skill':skill})

allow_access_to([User.SUPER_ADMIN])
def super_admin_update_skill_view(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    form = AddSkill(request.POST, instance=skill)
    if form.is_valid():
        form.save()
        messages.success(request, "Skill added successfully")

    form = AddSkill(instance=skill)
    return render(request, 'dashboard/super_admin/super_admin_update_skill.html', {'form':form})

@allow_access_to([User.SUPER_ADMIN])
def super_admin_delete_skill_view(request, pk):
    skill = Skill.objects.get(id=pk)
    skill.delete()
    messages.success(request, "Skill deleted successfully")
    return redirect('super_admin:super_admin_skill_list')
