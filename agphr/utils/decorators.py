from django.http import Http404
from functools import wraps
from users.models import User

  
def allow_access_to(user_type_list):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated:
                if user.user_type in user_type_list:
                    return func(request, *args, **kwargs)
                raise Http404
            raise Http404
        return wrapper
    return decorator
