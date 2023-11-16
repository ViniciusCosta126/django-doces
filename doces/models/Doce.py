from doces.models import models


class Doce(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(blank=True, null=True)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=1000, decimal_places=2)


    def __str__(self):
        return self.nome