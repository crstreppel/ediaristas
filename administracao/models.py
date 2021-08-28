from django.db import models

class Servico(models.Model):
    ICONE_CHOICES = (
        ('twf-cleaning1', 'twf-cleaning1'),
        ('twf-cleaning2', 'twf-cleaning2'),
        ('twf-cleaning2', 'twf-cleaning3'),
    )
    nome = models.CharField(max_length=50, null=False, blank=False)
    valor_minimo = models.FloatField(null=False, blank=False)
    qtd_horas = models.IntegerField(null=False, blank=False)
    porcentagem_comissao = models.FloatField(null=False, blank=False)
    horas_quarto = models.IntegerField(null=False, blank=False)
    valor_quarto = models.FloatField(null=False, blank=False)
    horas_sala = models.IntegerField(null=False, blank=False)
    valor_sala = models.FloatField(null=False, blank=False)
    horas_banheiro = models.IntegerField(null=False, blank=False)
    valor_banheiro = models.FloatField(null=False, blank=False)
    horas_cozinha = models.IntegerField(null=False, blank=False)
    valor_cozinha = models.FloatField(null=False, blank=False)
    horas_quintal = models.IntegerField(null=False, blank=False)
    valor_quintal = models.FloatField(null=False, blank=False)
    horas_outros = models.IntegerField(null=False, blank=False)
    valor_outros = models.FloatField(null=False, blank=False)
    icone = models.CharField(null=False, blank=False, choices=ICONE_CHOICES, max_length=14)
    posicao = models.IntegerField(null=False)