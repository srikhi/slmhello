from django.http import HttpResponse

def GoogleVerification(request):
    return HttpResponse(
            "google-site-verification: google3a6caebbf07938b8.html",
            content_type='text/plain')

def helloworld(request):
    return HttpResponse("Hello World!", content_type='text/plain')
