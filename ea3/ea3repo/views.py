from django.shortcuts import render
from .models import Artifact

def search_by_name(request):
    query = request.GET.get('q')
    artifacts = Artifact.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'artifacts': artifacts})

def search_by_level_layer(request):
    level = request.GET.get('level')
    use_frequency = request.GET.get('use_frequency')
    artifacts = Artifact.objects.filter(level__name=level, use_frequency=use_frequency)
    return render(request, 'search_results.html', {'artifacts': artifacts})
