from doces.models import models,Categoria


class Doce(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(blank=True, null=True)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=1000, decimal_places=2)
    categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE,related_name='categoria')


    def __str__(self):
        return self.nome