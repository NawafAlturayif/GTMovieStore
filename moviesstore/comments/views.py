from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from movies.models import Review

def index(request):
    template_data = {}
    template_data['title'] = 'Comments'
    template_data['reviews'] = Review.objects.all()


    return render(request, 'comments/index.html', {
        'template_data': template_data})
