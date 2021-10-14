from django.shortcuts import render

def main_index(request):
    context = {'title': 'Job Finder', }
    return render(request, "main_index.html", context)