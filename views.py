from django.shortcuts import render

from .models import Feed

def index(request):
    return render(request, 'feeds/index.html', {
        'feeds': Feed.objects.all().order_by('created')
    })
