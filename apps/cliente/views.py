from django.shortcuts import render

########################################################################## HOME
def home(request):
  return render(request, 'home.html')

def convenios(request):
  return render(request, 'cliente/convenios.html')

def financeiro(request):
  return render(request, 'cliente/financeiro.html')

def novaConsulta(request):
  return render(request, 'cliente/nova_consulta.html')

def novoExame(request):
  return render(request, 'cliente/novo_exame.html')

################################################################## MINHAS GUIAS
def mgSolicitadas(request):
  return render(request, 'cliente/mg1-solicitadas.html')
def mgAprovadas(request):
  return render(request, 'cliente/mg2-aprovadas.html')

def mgFaturadas(request):
  return render(request, 'cliente/mg3-faturadas.html')

def mgAuditadas(request):
  return render(request, 'cliente/mg4-auditadas.html')

def mgCanceladas(request):
  return render(request, 'cliente/mg5-canceladas.html')

###############################################################################