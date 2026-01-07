from django.shortcuts import render

def home(request):
    """
    Displays the home page of the Knowledge Learning platform.
    """
    return render(request, 'home.html')
