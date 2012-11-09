from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.reverse import reverse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
#from skifflog.serializers import UserSerializer, GroupSerializer

@api_view(['GET'])
def home(request):
    if request.user.is_active:
        return redirect('dashboard')
    return Response({'hi': 'ho'}, template_name='home.html')

def profile(request):
    return redirect('dashboard')

@api_view(['GET'])
@login_required
def dashboard(request):
    return Response({'hi': 'ho'}, template_name='dashboard.html')
