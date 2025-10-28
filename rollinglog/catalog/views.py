from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to RollingLog Catalog<h1>')

def about(request):
    return HttpResponse('<h1>About RollingLog</h1><p>Your personal rolling paper catalog.</p>')
