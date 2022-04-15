from django.forms import ModelForm
from api.models import Alarm

class AlarmForm(ModelForm):
    class Meta:
        model = Alarm
        fields = ['title','time','color']
