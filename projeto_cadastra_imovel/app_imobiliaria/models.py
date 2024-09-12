from django.db import models

class Imovel(models.Model):
    TIPO_IMOVEL_CHOICES = [
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
    ]

    # Atributos comuns a ambos os tipos de imóveis
    id_imovel = models.AutoField(primary_key=True)
    tipo_imovel = models.CharField(max_length=20, choices=TIPO_IMOVEL_CHOICES)
    nome_proprietario = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    quantidade_quartos = models.PositiveIntegerField()
    quantidade_suites = models.PositiveIntegerField()
    quantidade_salas_estar = models.PositiveIntegerField()
    vagas_garagem = models.PositiveIntegerField()
    area = models.DecimalField(max_digits=8, decimal_places=2)  
    armario_embutido = models.BooleanField()
    descricao = models.TextField(blank=True, null=True)
    valor_imovel = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imagem_imovel = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

    # Atributos específicos para casa
class Casa(models.Model):
        imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE, primary_key=True)

    # Atributos específicos para apartamento
class Apartamento(models.Model):
        imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE, primary_key=True)
        quantidade_salas_jantar = models.PositiveIntegerField()
        andar = models.PositiveIntegerField()
        valor_condominio = models.DecimalField(max_digits=8, decimal_places=2)
        portaria_24h = models.BooleanField()

def __str__(self):
    return f'{self.tipo_imovel} - {self.nome_proprietario}'


class Visita(models.Model):
    endereco = models.CharField(max_length=255)
    imovel = models.ForeignKey('Imovel', on_delete=models.CASCADE)
    data_visita = models.DateField()
    horario_visita = models.TimeField()

    def __str__(self):
        return f'Visita em {self.endereco} no dia {self.data_visita}'
