from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.reverse import reverse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
#from skifflog.serializers import UserSerializer, GroupSerializer

@api_view(['GET'])
def home(request):
    return Response({'hi': 'ho'}, template_name='home.html')

def dash(request):
    return Response()

def login(request):
    return "DICKS"