from django.forms import ModelForm
from django.forms.widgets import TextInput
from api.models import Alarm

class AlarmForm(ModelForm):
    class Meta:
        model = Alarm
        fields = ['title','time','color']
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }
        
