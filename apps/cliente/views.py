from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from cliente.models import TesteConsultas
from cliente.forms import TesteConsultasForm

########################################################################## HOME
@login_required(login_url='/login/')
def home(request):
  if request.device['is_mobile']:
    return render(request, 'home-mobile.html')
  else:
    return render(request, 'home.html')

##################################################################### CONVENIOS
@login_required(login_url='/login/')
def convenios(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/convenios.html')
  else:
    return render(request, 'cliente/convenios.html')

#################################################################### FINANCEIRO
@login_required(login_url='/login/')
def financeiro(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/financeiro.html')
  else:
    return render(request, 'cliente/financeiro.html')

################################################################# NOVA CONSULTA
@login_required(login_url='/login/')
def novaConsulta(request):

  if request.method == 'POST':
    form = TesteConsultasForm(request.POST)

    if form.is_valid():
      item = form.save(commit=False)
      item.usuario = str(request.user.username)
      item.save()
      return redirect('/cliente/mg_solicitadas/')
    
  else: 
    form = TesteConsultasForm()

    if request.device['is_mobile']:
      return render(request, 'cliente-mob/nova_consulta.html', {'form':form})
    else:
      return render(request, 'cliente/nova_consulta.html', {'form':form})
    
#################################################################### NOVO EXAME
@login_required(login_url='/login/')
def novoExame(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/novo_exame.html')
  else:
    return render(request, 'cliente/novo_exame.html')

################################################################## MINHAS GUIAS

################################################################### SOLICITADAS
@login_required(login_url='/login/')
def mgSolicitadas(request):
  consultas = TesteConsultas.objects.filter(situacao='Solicitada')

  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg1-solicitadas.html', {'consultas':consultas})
  else:
    return render(request, 'cliente/mg1-solicitadas.html', {'consultas':consultas})

##################################################################### APROVADAS
@login_required(login_url='/login/')
def mgAprovadas(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg2-aprovadas.html')
  else:
    return render(request, 'cliente/mg2-aprovadas.html')

##################################################################### FATURADAS
@login_required(login_url='/login/')
def mgFaturadas(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg3-faturadas.html')
  else:
    return render(request, 'cliente/mg3-faturadas.html')

##################################################################### AUDITADAS
@login_required(login_url='/login/')
def mgAuditadas(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg4-auditadas.html')
  else:
    return render(request, 'cliente/mg4-auditadas.html')

#################################################################### CANCELADAS
@login_required(login_url='/login/')
def mgCanceladas(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg5-canceladas.html')
  else:
    return render(request, 'cliente/mg5-canceladas.html')

###############################################################################