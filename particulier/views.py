from django.shortcuts import render

# Create your views here.
def particulier_views(request):
    template_name = 'particulier/particulier_home.html'
    context = {}
    return render(request, template_name, context)