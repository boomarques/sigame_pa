from django.contrib import admin
from django.urls import include, path
from apps.cliente import views as clienteViews

urlpatterns = [
#============================================================================================ ADMIN
  path('admin/', admin.site.urls),
  path('', include('django.contrib.auth.urls')),

#============================================================================================= HOME
  path('', clienteViews.home, name='home'),
  path('cliente/convenios/', clienteViews.convenios, name='convenios'),
  path('cliente/financeiro/', clienteViews.financeiro, name='financeiro'),
  path('cliente/nova_consulta/', clienteViews.novaConsulta, name='nova-consulta'),
  path('cliente/novo_exame/', clienteViews.novoExame, name='novo-exame'),

#===================================================================================== MINHAS GUIAS
  path('cliente/mg_solicitadas/', clienteViews.mgSolicitadas, name='mg-solicitadas'),
  path('cliente/mg_aprovadas/', clienteViews.mgAprovadas, name='mg-aprovadas'),
  path('cliente/mg_faturadas/', clienteViews.mgFaturadas, name='mg-faturadas'),
  path('cliente/mg_auditadas/', clienteViews.mgAuditadas, name='mg-auditadas'),
  path('cliente/mg_canceladas/', clienteViews.mgCanceladas, name='mg-canceladas'),
#==================================================================================================
]
