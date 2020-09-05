from django.shortcuts import render

# Create your views here.
def home_views(request):
    template_name = 'pages/app/home.html'
    return render(request, template_name, context=None)

def contact_views(request):
    template_name = 'pages/app/contact.html'
    return render(request, template_name, context=None)

def about_views(request):
    template_name = 'pages/app/about.html'
    return render(request, template_name, context=None)
