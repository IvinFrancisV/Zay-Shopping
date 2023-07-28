from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request ,"index.html")


def view_about(request):
    return render(request, "about_us.html")
