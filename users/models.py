from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
                                        BaseUserManager, 
                                        PermissionsMixin
                                        )

class UserManager(BaseUserManager):
    def _create_user(self, email, mobile, password=None, **extra_fields):
        if not mobile and not email:
            raise ValueError('Users must have either an email or mobile number')

        if email:
            email = self.normalize_email(email)
        mobile = self.normalize_mobile(mobile) if mobile else None
        user = self.model(email=email, mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, mobile=None, password=None, **extra_fields):
        return self._create_user(email, mobile, password, **extra_fields)

    def create_superuser(self, email=None, mobile=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, mobile, password, **extra_fields)
    
    def normalize_mobile(self, mobile):
        # Remove whitespace and special characters
        normalized_mobile = ''.join(filter(str.isdigit, mobile))
        return normalized_mobile
    
class User(AbstractBaseUser, PermissionsMixin):
    SUPER_ADMIN = "Super Admin"
    EMPLOYER = "Employer"
    APPLICANT_USER = "Applicant User"

    USER_TYPE_CHOICES = (
        (SUPER_ADMIN, SUPER_ADMIN),
        (EMPLOYER, EMPLOYER),
        (APPLICANT_USER, APPLICANT_USER),
    )

    email = models.EmailField('email address', unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField('mobile number', max_length=10, unique=True, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="user_profile_pics/%Y/%m/%d", null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=APPLICANT_USER)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff status', default=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email if self.email else str(self.mobile)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
