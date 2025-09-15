from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    return render(request, 'home/index.html', {
        'template_data': template_data})
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html',
                  {'template_data': template_data})

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        try:
            repo = git.Repo("/home/Nawaf1099901/GTMovieStore")
            origin = repo.remotes.origin
            origin.pull()
            return HttpResponse("Updated server successfully")
        except Exception as e:
            return HttpResponse(str(e), status=500)
    return HttpResponse("Couldn't update the server", status=400)