from django.db import models

class About(models.Model):
    descripcion_corta = models.TextField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="about")


    class Meta:
        verbose_name= "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"
    

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    descripcion = models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name
    

class RecentWork(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Work title")
    imagen = models.ImageField(upload_to="works")


    def __str__(self):
        return self.titulo
    

class Client(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Client name")
    descripcion = models.TextField(verbose_name="Client say")
    imagen = models.ImageField(upload_to="clients", default="default.png")


    def __str__(self):
        return self.nombre
    

