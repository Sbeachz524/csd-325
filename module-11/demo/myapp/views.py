from django.http import HttpResponse

def home(request):
    return HttpResponse("Beacham says Hello!")
