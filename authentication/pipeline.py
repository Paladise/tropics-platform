from authentication.models import User

def create_user(backend, user, response, *args, **kwargs):
    print("CREATING USER:")
    print("backend:", backend)
    print("user:", user)
    print("response:", response)
    print("args:", args)
    print("kwargs:", kwargs)

    if user:
        return {'is_new': False}

    u = User()

    for k, v in kwargs["details"].items():
        setattr(u, k, v)

    u.save()

    return {
        'is_new': True,
        'user': u
    }