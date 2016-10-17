
from django.core.exceptions import ImproperlyConfigured


def get_environment_var(env_name):
    try:
        import os
        return os.environ.get(env_name)
    except:
        err_msg = "The environmental variable %s is not found" % env_name
        raise ImproperlyConfigured(err_msg)


ENV_MODE = get_environment_var('ENV')
