from django.forms import ModelForm
from skifflog.models import UserProfile


class UserProfileForm(ModelForm):
     class Meta:
         model = UserProfile
         fields = ('membership', 'round_up')
