from django.conf import settings
from django.contrib.auth.middleware import get_user
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.utils.functional import SimpleLazyObject
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.rstrip('/'))]

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.require_login_path = getattr(settings,
                                          'LOGIN_URL',
                                          '/accounts/login/')
        # One-time configuration and initialization.

    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).

    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """
    @staticmethod
    def get_slm_user(request):
        assert hasattr(request, 'user'), "The Login Required middleware\
                requires authentication middleware to be installed. Edit your\
                MIDDLEWARE_CLASSES setting to insert\
                'django.contrib.auth.middleware.AuthenticationMiddleware'. If \
                that doesn't work, ensure your TEMPLATE_CONTEXT_PROCESSORS \
                setting includes 'django.core.context_processors.auth'."
        user = get_user(request)
        if user.is_authenticated():
            return user
        return None


    def __call__(self, request):
        request.user = SimpleLazyObject(
                                lambda: self.__class__.get_slm_user(request))
        if request.user is None:
            request.path = '%s?next=%s' % (self.require_login_path,
                                           request.get_full_path)
    def __call__(self, request):
        user = get_user(request)
        if user.is_authenticated():
            return self.get_response(request)

        path = request.path_info.lstrip('/')
        for m in EXEMPT_URLS:
            if m.match(path):
                return self.get_response(request)

        return HttpResponseRedirect('%s?next=%s' % (self.require_login_path,
                                                    request.path))
