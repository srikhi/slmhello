import textwrap

from django.http import HttpResponse
from django.views.generic.base import View

def GoogleVerification(request):
    return HttpResponse(
            "google-site-verification: google3a6caebbf07938b8.html",
            content_type='text/plain')

def helloworld(request):
    return HttpResponse("Hello World!", content_type='text/plain')

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
