from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "home.html", {})


def cert(request):
    return render(request, "cert.html", {})
