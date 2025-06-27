from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()

    # ManyToMany simples com Categoria
    categorias = models.ManyToManyField(Categoria, related_name='livros')

    # ManyToMany com campo extra com Autor
    autores = models.ManyToManyField(Autor, through='LivroAutor', related_name='livros_com_ordenacao')

    def __str__(self):
        return self.titulo


class LivroAutor(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ordem_autoria = models.IntegerField()

    def __str__(self):
        return f"{self.autor.nome} - {self.livro.titulo} (Ordem: {self.ordem_autoria})"
