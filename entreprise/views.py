from django.shortcuts import render

# Create your views here.

def entreprise_home(request):
    template_name = 'pages/entreprise/entreprise_home.html'
    context = None
    return render(request, template_name, context)
