from django.shortcuts import render

from rest_framework import viewsets  # import 
from .models import customer, rocket, payload, launch
from .serializers import customerSerializer, rocketSerializer, payloadSerializer, launchSerializer

from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    urls = {
        'customer': reverse('customer-list', request=request, format=format),
        'rocket': reverse('rocket-list', request=request, format=format),
        'payload': reverse('payload-list', request=request, format=format),
        'launch': reverse('launch-list', request=request, format=format),
    }

    # Modify the URLs to use HTTPS
    for key, url in urls.items():
        urls[key] = url.replace('http://', 'https://')

    return Response(urls)


class customerViewSet(viewsets.ModelViewSet):
    serializer_class = customerSerializer
    queryset = customer.objects.all()
    
    
class rocketViewSet(viewsets.ModelViewSet):
    serializer_class = rocketSerializer
    queryset = rocket.objects.all()
    
    
class payloadViewSet(viewsets.ModelViewSet):
    serializer_class = payloadSerializer
    queryset = payload.objects.all()
    
    
class launchViewSet(viewsets.ModelViewSet):
    serializer_class = launchSerializer
    queryset = launch.objects.all()