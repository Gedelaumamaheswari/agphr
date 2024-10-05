from django.db import models
from django.urls import reverse
from job.models import Skill
from users.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
import os

def validate_file_size(file):
    limit = 2 * 1024 * 1024  # 2 MB
    if file.size > limit:
            raise ValidationError(f"File size should not exceed {limit / (1024 * 1024):.2f} MB. Current size: {file.size / (1024 * 1024):.2f} MB.")
 
class Applicant(models.Model):
    EXPERIENCE_INTERN_LEVEL = "Intern"
    EXPERIENCE_ENTRY_LEVEL = "Entry Level"
    EXPERIENCE_MID_LEVEL = "Mid Level"
    EXPERIENCE_SENIOR_LEVEL = "Senior Level"
    EXPERIENCE_MANAGEMENT_LEVEL = "Management Level"
    EXPERIENCE_EXECUTIVE_LEVEL = "Executive Level"

    EXPERIENCE_LEVEL_CHOICES = (
        (EXPERIENCE_INTERN_LEVEL, EXPERIENCE_INTERN_LEVEL),
        (EXPERIENCE_ENTRY_LEVEL, EXPERIENCE_ENTRY_LEVEL),
        (EXPERIENCE_MID_LEVEL, EXPERIENCE_MID_LEVEL),
        (EXPERIENCE_SENIOR_LEVEL, EXPERIENCE_SENIOR_LEVEL),
        (EXPERIENCE_MANAGEMENT_LEVEL, EXPERIENCE_MANAGEMENT_LEVEL),
        (EXPERIENCE_EXECUTIVE_LEVEL, EXPERIENCE_EXECUTIVE_LEVEL),
    )

    HIGHEST_EDUCATION_HIGH_SCHOOL = "High School"
    HIGHEST_EDUCATION_ASSOCIATE_DEGREE = "Associate Degree"
    HIGHEST_EDUCATION_BACHELORS_DEGREE = "Bachelor's Degree"
    HIGHEST_EDUCATION_MASTERS_DEGREE = "Master's Degree"
    HIGHEST_EDUCATION_DOCTORATE = "Doctorate"

    HIGHEST_EDUCATION_CHOICES = (
        (HIGHEST_EDUCATION_HIGH_SCHOOL, HIGHEST_EDUCATION_HIGH_SCHOOL),
        (HIGHEST_EDUCATION_ASSOCIATE_DEGREE, HIGHEST_EDUCATION_ASSOCIATE_DEGREE),
        (HIGHEST_EDUCATION_BACHELORS_DEGREE, HIGHEST_EDUCATION_BACHELORS_DEGREE),
        (HIGHEST_EDUCATION_MASTERS_DEGREE, HIGHEST_EDUCATION_MASTERS_DEGREE),
        (HIGHEST_EDUCATION_DOCTORATE, HIGHEST_EDUCATION_DOCTORATE),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='applicant',
        verbose_name="User"
    )
    resume = models.FileField(
        upload_to="resumes/%Y/%m/%d/",
        validators=[validate_file_size],
        help_text="Upload your resume in PDF or Word format.",
        verbose_name="Resume"
    )
    bio = models.TextField(
        blank=True,
        null=True,
        validators=[MaxLengthValidator(500)],
        help_text="A brief summary about yourself and your career (max 500 characters).",
        verbose_name="Bio"
    )
    current_job_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Your current job title.",
        verbose_name="Current Job Title"
    )
    skills = models.ManyToManyField(
        Skill,
        related_name='applicants',
        blank=True,
        help_text="Select the skills you possess.",
        verbose_name="Skills"
    )
    linkedin_profile = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Link to your LinkedIn profile.",
        verbose_name="LinkedIn Profile"
    )
    github_profile = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Link to your GitHub profile.",
        verbose_name="GitHub Profile"
    )
    portfolio_website = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Link to your portfolio website.",
        verbose_name="Portfolio Website"
    )
    experience_level = models.CharField(
        max_length=50,
        choices=EXPERIENCE_LEVEL_CHOICES,
        blank=True,
        null=True,
        help_text="Select your overall experience level.",
        verbose_name="Experience Level"
    )
    years_of_experience = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Enter the total years of professional experience.",
        verbose_name="Years of Experience"
    )
    highest_education = models.CharField(
        max_length=100,
        choices=HIGHEST_EDUCATION_CHOICES,
        blank=True,
        null=True,
        help_text="Select your highest level of education.",
        verbose_name="Your Highest Education"
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Your current city.",
        verbose_name="City"
    )
    state = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Your current state.",
        verbose_name="State"
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Your current country.",
        verbose_name="Country"
    )
    is_available_for_work = models.BooleanField(
        default=True,
        help_text="Are you currently looking for work?",
        verbose_name="Available for Work"
    )
    willing_to_relocate = models.BooleanField(
        default=False,
        help_text="Are you willing to relocate for a job?",
        verbose_name="Willing to Relocate"
    )
    desired_salary = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Expected salary (e.g., $60,000 per year).",
        verbose_name="Desired Salary"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - Applicant'

    class Meta:
        verbose_name = 'Applicant Profile'
        verbose_name_plural = 'Applicant Profiles'

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_skills_list(self):
        return ', '.join(skill.name for skill in self.skills.all())

    def clean(self):
        super().clean()
        if self.resume:
            valid_extensions = ['.pdf', '.doc', '.docx']
            ext = os.path.splitext(self.resume.name)[1]
            if ext.lower() not in valid_extensions:
                raise ValidationError("Only PDF and Word documents are allowed for the resume.")