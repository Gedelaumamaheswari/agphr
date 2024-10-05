from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from agphr.utils.decorators import allow_access_to
from django.db import transaction
from users.models import User
from applicant.models import Applicant
from applicant.forms import (ApplicantUserForm, 
                             ApplicantForm, 
                             ApplicantProfileForm, 
                             ApplicantUserProfileForm
							)
from job.models import Job
import logging

@allow_access_to([User.APPLICANT_USER])
def applicant_analytics_view(request,):
  return render(request, 'dashboard/applicant/applicant_analytics.html')

def apply_job(request, slug):
    job = get_object_or_404(Job, slug=slug)
    user=request.user
    check_applied_condition = 1 in [job.is_applied for job in job.jobapplicant_set.all().filter(user=user)]
    if check_applied_condition:
        return redirect("job:job_detail", slug=job.slug)
    try:
        applicant = Applicant.objects.get(user=user)
    except:
        applicant=None
    if request.method=="POST":
        user_form = ApplicantUserForm(request.POST, request.FILES, instance=user)
        applicant_form = ApplicantForm(request.POST, request.FILES, instance=applicant)
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
                        applicant = Applicant.objects.get(user=user)
                        applicant.notice_period=notice_period
                        applicant.resume=resume
                        applicant.linkedin_link=linkedin_link
                        applicant.qualitative_skills=qualitative_skills
                        applicant.subject=subject
                        applicant.message=message
                    except:
                        applicant = Applicant(
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

@allow_access_to([User.APPLICANT_USER])   
def applicant_profile_view(request):
    user = request.user
    applicant = Applicant.objects.filter(user=user).first()
    if request.method=="POST":
        applicant_user_form = ApplicantUserProfileForm(request.POST, request.FILES, instance=user)
        applicant_profile_form = ApplicantProfileForm(request.POST, request.FILES, instance=applicant)
        if applicant_user_form.is_valid() and applicant_profile_form.is_valid():
            applicant_user_form.save()
            applicant_profile_form = applicant_profile_form.save(commit=False)
            applicant_profile_form.user = request.user
            applicant_profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("applicant:applicant_profile")
        else:
             context = {
                 'applicant_user_form': applicant_user_form,
                 'applicant_profile_form': applicant_profile_form 
                 }
             return render(request, 'dashboard/applicant/applicant_profile.html', context)
    else:
        applicant_profile_form = ApplicantProfileForm(instance=applicant)
        applicant_user_form = ApplicantUserProfileForm(instance=user)
        context = {
                 'applicant_profile_form': applicant_profile_form, 
                 'applicant_user_form': applicant_user_form
                 }
        return render(request, 'dashboard/applicant/applicant_profile.html', context)