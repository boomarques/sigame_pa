from django import forms
from .models import TesteConsultas

class TesteConsultasForm(forms.ModelForm):
  class Meta:
    model = TesteConsultas
    fields = ('especialidade', 'local')
