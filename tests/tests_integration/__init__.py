import pytest
import os


def dedicated_app_tokens_exist():
    try:
        os.environ['MKM_APP_TOKEN']
        os.environ['MKM_APP_SECRET']
        os.environ['MKM_ACCESS_TOKEN']
        os.environ['MKM_ACCESS_TOKEN_SECRET']
        return True
    except KeyError:
        return False


def widget_app_tokens_exist():
    try:
        os.environ['MKM_APP_TOKEN']
        os.environ['MKM_APP_SECRET']
        return True
    except KeyError:
        return False


missing_app_tokens = pytest.mark.skipif(not dedicated_app_tokens_exist(), reason='Missing dedicated app tokens')
missing_widget_tokens = pytest.mark.skipif(not widget_app_tokens_exist(), reason='Missing widget app tokens')
