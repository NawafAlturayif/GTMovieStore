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
import logging

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        try:
            logging.basicConfig(filename='/tmp/webhook.log', level=logging.INFO)
            logging.info('Webhook received')
            return HttpResponse("Webhook received successfully")
        except Exception as e:
            # This part should not be reached, but it's good to have it
            return HttpResponse(str(e), status=500)
    return HttpResponse("Couldn't update the server", status=400)