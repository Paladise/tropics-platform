from authentication.models import User

def create_user(backend, user, response, *args, **kwargs):
    if user:
        return {'is_new': False}

    u = User()

    for k, v in kwargs["details"].items():
        setattr(u, k, v)

    u.set_unusable_password() # To prevent annoying popup in Admin interface
    u.save()

    return {
        'is_new': True,
        'user': u
    }