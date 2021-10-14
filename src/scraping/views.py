from django.shortcuts import render

def main_navbar(request):
    context = {'title': 'Job Finder', }
    return render(request, "Navbar.html", context)


