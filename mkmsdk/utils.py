import os
from . import exceptions


def _get_env_var(key):
    try:
        return os.environ[key]
    except KeyError:
        raise exceptions.MissingEnvVar(key)


def get_mkm_app_token():
    return _get_env_var('MKM_APP_TOKEN')


def get_mkm_app_secret():
    return _get_env_var('MKM_APP_SECRET')


def get_mkm_access_token():
    return _get_env_var('MKM_ACCESS_TOKEN')


def get_mkm_access_token_secret():
    return _get_env_var('MKM_ACCESS_TOKEN_SECRET')
