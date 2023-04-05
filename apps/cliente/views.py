from django.shortcuts import render

########################################################################## HOME
def home(request):
  
  if request.device['is_mobile']:
    return render(request, 'home-mobile.html')
  else:
    return render(request, 'home.html')

def convenios(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/convenios.html')
  else:
    return render(request, 'cliente/convenios.html')

def financeiro(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/financeiro.html')
  else:
    return render(request, 'cliente/financeiro.html')

def novaConsulta(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/nova_consulta.html')
  else:
    return render(request, 'cliente/nova_consulta.html')

def novoExame(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/novo_exame.html')
  else:
    return render(request, 'cliente/novo_exame.html')

################################################################## MINHAS GUIAS
def mgSolicitadas(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg1-solicitadas.html')
  else:
    return render(request, 'cliente/mg1-solicitadas.html')

def mgAprovadas(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg2-aprovadas.html')
  else:
    return render(request, 'cliente/mg2-aprovadas.html')

def mgFaturadas(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg3-faturadas.html')
  else:
    return render(request, 'cliente/mg3-faturadas.html')

def mgAuditadas(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg4-auditadas.html')
  else:
    return render(request, 'cliente/mg4-auditadas.html')

def mgCanceladas(request):
  if request.device['is_mobile']:
    return render(request, 'cliente-mob/mg5-canceladas.html')
  else:
    return render(request, 'cliente/mg5-canceladas.html')

###############################################################################