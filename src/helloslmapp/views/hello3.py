from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import textwrap


class AuthHomePageView(TemplateView):

    @method_decorator(login_required)
    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Hello SLM World</title>
            </head>
            <body>
                <h1>Greetings from SLM World</h1>
                <p>Hello, User !</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)
