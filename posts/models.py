from django.db import models

class Categoria(models.Model):
    ca_nombre = models.CharField(max_length=30,verbose_name="nombre")
    ca_descripcion = models.CharField(max_length=250)

    def __str__ (self):
        return self.nombre

class Autor(models.Model):
    au_nombre = models.CharField(max_length=30,verbose_name="nombre")
    au_especialidad = models.ForeignKey(Categoria,null=True,blank=True,on_delete=models.CASCADE)

    def __str__ (self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50,verbose_name="titulo")
    descripcion = models.CharField(max_length=100)
    img = models.CharField(max_length=240)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    f_categoria = models.IntegerField()

    def __str__ (self):
        return self.titulo

class Comentario(models.Model):
    com_contenido = models.CharField(max_length=150,verbose_name='com_contenido')
    f_post_id = models.IntegerField()
    com_fechaComentario = models.DateTimeField(auto_now_add=True, null=True)
        