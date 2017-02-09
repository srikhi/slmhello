import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class HomePageView(View):
    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Hello SLM World</title>
            </head>
            <body>
                <h1>Greetings from SLM World</h1>
                <p>Hello, world! -- SLM Gang</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)
