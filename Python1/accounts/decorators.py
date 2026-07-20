from django.core.exceptions import PermissionDenied

def role_required(required_role):
    def decorator(view_func):
        def wrapped(request, *args, **kwargs):
            if request.user.role != required_role:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return wrapped
    return decorator