from django.db import models
from django.contrib.auth import get_user_model

class TesteConsultas (models.Model) :
  # constantes
  ESPECIALIDADE = (
    ('Alergologia', 'Alergologia'),
    ('Clínico Geral', 'Clínico Geral'),
    ('Dermatologia', 'Dermatologia'),
    ('Endocrinologia', 'Endocrinologia'),
    ('Ginecologia', 'Ginecologia'),
    ('Geriatria', 'Geriatria'),
    ('Mastologia', 'Mastologia'),
    ('Nefrologia', 'Nefrologia'),
    ('Neurologia', 'Neurologia'),
    ('Nutricionista', 'Nutricionista'),
    ('Nutrologia', 'Nutrologia'),
    ('Obstetrícia', 'Obstetrícia'),
    ('Oftalmologia', 'Oftalmologia'),
    ('Ortopedia', 'Ortopedia'),
    ('Otorrinolaringologia', 'Otorrinolaringologia'),
    ('Pediatria', 'Pediatria'),
    ('Psicologia', 'Psicologia'),
    ('Psiquiatria', 'Psiquiatria'),
  )
  
  LOCAL = (
    ('Centro Médico do Porto', 'Centro Médico do Porto'),
    ('Clínica Lisboa', 'Clínica Lisboa'),
    ('Hospital Vila Nova de Gaia', 'Hospital Vila Nova de Gaia'),
  )

  SITUACAO = (
    ('Solicitada','Solicitada'),
    ('Aprovada', 'Aprovada'),
    ('Faturada', 'Faturada'),
    ('Auditada', 'Auditada'),
    ('Cancelada', 'Cancelada'),
  )
  
  # dados no db
  # usuario = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
  usuario = models.CharField(max_length=10)

  especialidade = models.CharField( max_length=25, choices=ESPECIALIDADE )

  local = models.CharField( max_length=50, choices=LOCAL )

  situacao = models.CharField( max_length=20, choices=SITUACAO, default='Solicitada')

  valor = models.DecimalField(max_digits=9, decimal_places=2, default=0)
  
  criacao = models.DateTimeField( auto_now_add=True )

  acompanhamento = models.TextField(blank=True)

  def __str__(self):
    # return self.usuario
    return 'C-' + str(self.id)
  

