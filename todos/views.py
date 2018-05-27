from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.views.generic import ListView
from .models import Deploy


class HomePageView(ListView):
    model = Deploy
    template_name = 'home.html'


def deploy_detail(request, deploy_id):
    deploy = get_object_or_404(Deploy, id=deploy_id)
    return render(request, 'deploy_detail.html', {'deploy': deploy})
