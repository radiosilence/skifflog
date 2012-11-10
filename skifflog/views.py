from copy import copy
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.utils.timezone import utc
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.reverse import reverse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from skifflog.forms import UserProfileForm
from skifflog.models import Block
from skifflog.serializers import BlockSerializer
from skifflog.utils import block_total, use_percentage

@api_view(['GET'])
def home(request):
    if request.user.is_active:
        return redirect('dashboard')
    return Response({}, template_name='home.html')

def profile(request):
    return redirect('dashboard')


@api_view(['GET', 'POST'])
@login_required
def debug(request):
    return Response({
        'user': repr(request.user),
        'session': repr(request.session),
        'visit': repr(request.session.get('visit', None))
    })


@api_view(['POST'])
@login_required
def arrive(request):
    profile = request.user.profile
    visit = profile.current_visit
    if not visit:
        visit = datetime.datetime.utcnow().replace(tzinfo=utc)
        profile.current_visit = visit
        profile.save()
    return Response({
        'visit': visit
    })


@api_view(['POST'])
@login_required
def depart(request):
    try:
        comment = request.DATA['comment']
    except:
        comment = ''

    profile = request.user.profile
    visit = copy(profile.current_visit)
    profile.current_visit = None
    profile.save()
    if not visit:
        return Response({
            'error': 'No visit started.'
        })
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    block = Block.objects.create(
        user=request.user,
        start=visit,
        duration=now - visit,
        comment=comment
    )

    block.save()
    return Response({
        'visit': visit,
        'duration': str(now - visit),
        'comment': comment
    })


@api_view(['GET'])
@login_required
def check(request):
    profile = request.user.profile
    visit = profile.current_visit
    if visit:
        return Response({
            'visit': visit
        })
    else:
        return Response({
            'error': 'No visit started.'
        })


@api_view(['GET', 'POST'])
@login_required
def dashboard(request):
    profile = request.user.profile
    profile_form = UserProfileForm(request.DATA, instance=profile)
    if profile_form.is_valid():
        profile_form.save()
    blocks = profile.month_blocks.order_by('-start')
    month_total = profile.used_time
    max_use = profile.max_use
    if max_use > datetime.timedelta(0):
        month_percentage = use_percentage(month_total, max_use)
    else:
        month_percentage = None
    serializer = BlockSerializer(blocks)
    context = {
        'max_use': max_use,
        'month': {
            'blocks': serializer.data,
            'total': month_total,
            'percentage': month_percentage,
        },
        'visit': profile.current_visit,
        'profile_form': profile_form
    }
    return Response(context, template_name='dashboard.html')
