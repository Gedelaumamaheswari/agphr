from django.contrib import messages
from hitcount.views import HitCountDetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db import transaction
from django.http import JsonResponse
from django.views.generic import ListView
from job.forms import JobApplicantForm, JobApplicantUserForm
from job.models import Job, JobApplicant, Skill
import logging
User = get_user_model()

@csrf_exempt
def search(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "GET":
        if 'term' in request.GET:
            term = request.GET.get("term")
            skill_queryset = Skill.objects.filter(Q(name__icontains=term))
            job_queryset = Job.objects.filter(Q(job_title__icontains=term))
    
            skill_query = [query.name for query in skill_queryset]
            job_query =[query.job_title for query in job_queryset]
            list_queryset = skill_query + job_query
        if 'location' in request.GET:
            location = request.GET.get("location")
            queryset = Job.objects.filter(Q(place__icontains=location))
            list_queryset = [query.place for query in queryset] 

        unique_list_queryset = list(dict.fromkeys(list_queryset))
        return JsonResponse(unique_list_queryset, safe=False)   

class HomeView(ListView):
    model = Job
    template_name = 'home.html'
    context_object_name = 'jobs'
    def get_queryset(self, *args, **kwargs):
        return Job.objects.recommended_jobs()

from django.template.loader import render_to_string
class JobList(ListView):
    model = Job
    template_name = 'job/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10
    
    def get_queryset(self):
        locations = self.request.GET.get('locations')
        skills = self.request.GET.get('skills')
        object_list = Job.objects.published_job_lists()

        location_lists = []
        skill_lists = []

        if locations:
            location_lists = [location.strip() for location in locations.split(",") if location.strip()]

        if skills:
            skill_lists = [skill.strip() for skill in skills.split(",") if skill.strip()]

            search_skills = location_lists + skill_lists
            object_list = Job.objects.published_job_lists(search_skills)        
            job_length = len(object_list)
            if job_length < 1 :
                object_list = Job.objects.published_job_lists()
                messages.warning(self.request, "No job found.")
            else:
                messages.success(self.request, f"{job_length} Job found.")
        return object_list[:31]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_title = self.request.GET.get('job_title')
        if job_title:
            try:
                job = Job.objects.get(slug=job_title)
                context['job'] = job
            except Job.DoesNotExist:
                messages.error(self.request, "The requested job was not found.")
                context['job'] = None
        else:
            # If no specific job is requested, default to the first job in the object_list
            job_list = context.get('jobs')
            if job_list:
                context['job'] = job_list[0]  # Set the first job as default
            else:
                context['job'] = None

        return context
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            jobs_html = render_to_string('partial.html', context)
            return JsonResponse({
                'jobs_html': jobs_html,
                'has_next': context['page_obj'].has_next(),
            })
        return super().render_to_response(context, **response_kwargs)
job_list = JobList.as_view()

@method_decorator(login_required, name='dispatch')
class JobDetail(HitCountDetailView):
    model = Job
    template_name = "job/job_detail.html"
    context_object_name = "job"
    slug_field = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user=self.request.user
        slug=self.kwargs.get('slug')
        skill=[skill.name for skill in self.object.skill_set.all()]
        object=self.object
        context['check_applied_condition'] = 1 in [job.is_applied for job in Job.objects.get(slug=slug).jobapplicant_set.all().filter(user=user)]
        context['similar_jobs'] = Job.objects.filter(country=object.country, place=object.place, skill__name__in=skill).distinct().exclude(slug=slug)

        try:
            applicant = JobApplicant.objects.get(user=user)
        except:
            applicant=None
        context['user_form'] = JobApplicantUserForm(instance=user)
        context['applicant_form'] = JobApplicantForm(instance=applicant)
        return context
job_detail = JobDetail.as_view()

@login_required
def apply_job(request, slug):
    job = get_object_or_404(Job, slug=slug)
    user=request.user
    check_applied_condition = 1 in [job.is_applied for job in job.jobapplicant_set.all().filter(user=user)]
    if check_applied_condition:
        return redirect("job:job_detail", slug=job.slug)
    try:
        applicant = JobApplicant.objects.get(user=user)
    except:
        applicant=None
    if request.method=="POST":
        user_form = JobApplicantUserForm(request.POST, request.FILES, instance=user)
        applicant_form = JobApplicantForm(request.POST, request.FILES, instance=applicant)
        if user_form.is_valid() and applicant_form.is_valid():
            resume=applicant_form.cleaned_data.get('resume')
            if resume.size > 2 * 1024 * 1024:
                logging.warning("Applicant attempted to upload large resume file.")
                messages.warning(request, "Resume too large. Size should not exceed 2 MiB.")
                return redirect("job:job_detail", slug=job.slug)

            notice_period=applicant_form.cleaned_data.get('notice_period')
            resume=applicant_form.cleaned_data.get('resume')
            name=user_form.cleaned_data.get('name')
            mobile=user_form.cleaned_data.get('mobile')

            linkedin_link=applicant_form.cleaned_data.get('linkedin_link')
            qualitative_skills=applicant_form.cleaned_data.get('qualitative_skills')
            subject=applicant_form.cleaned_data.get('subject')
            message=applicant_form.cleaned_data.get('message')
            try:
                with transaction.atomic():
                    user.name=name
                    user.mobile=mobile
                    user.save()
                    try:
                        applicant = JobApplicant.objects.get(user=user)
                        applicant.notice_period=notice_period
                        applicant.resume=resume
                        applicant.linkedin_link=linkedin_link
                        applicant.qualitative_skills=qualitative_skills
                        applicant.subject=subject
                        applicant.message=message
                    except:
                        applicant = JobApplicant(
                                    user=user,
                                    notice_period=notice_period,
                                    is_applied=1,
                                    resume=resume,
                                    linkedin_link=linkedin_link,
                                    qualitative_skills=qualitative_skills,
                                    subject=subject,
                                    message=message,
                                )
                    applicant.save()
                    applicant.job.add(job)
                    job.job_applied_count=job.job_applied_count + 1 if job.job_applied_count else 1
                    job.save()
                    messages.success(request, "You have succesfully applied for the job")
                    return redirect("job:job_detail", slug=job.slug)
            except:
                logging.info("Some error occured while applying the job")
                messages.warning(request, "Not able to apply, please try again")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.warning(request, "Something went wrong or not valid data")
            return redirect("job:job_detail", slug=job.slug)

@csrf_exempt
def skillSearch(request):
    if request.method == "GET":
        if 'term' in request.GET:
            term = request.GET.get("term")
            list_queryset = Skill.objects.filter(name__icontains=term)
            skills_list = [{"id": skill.id, "label": skill.name} for skill in list_queryset]
            print(skills_list)
            return JsonResponse(skills_list, safe=False)
def search_result(request):
    salary = request.GET.get("salary", None)
    freshness = request.GET.get("freshness", None)
    experience = request.GET.get("experience", None)
    country = request.GET.getlist("country", None)
    job_list = Job.objects.get_filtered_data(salary, freshness, experience, country)
    
    context = {'job_list':job_list,
               'freshness':freshness,
               'salary':salary,
               'experience':experience,
               }
    return render(request, 'job/search_result.html', context)