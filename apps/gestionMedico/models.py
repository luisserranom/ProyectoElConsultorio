from django.db import models

# Create your models here.
class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True,verbose_name="id especialidad")
    nombre_especialidad = models.CharField(max_length=50,verbose_name="nombre especialidad")

    class Meta:
        managed = False
        db_table = 'especialidad'
        
    def __str__(self):
        return '{}'.format(self.nombre_especialidad)

class Especialista(models.Model):
    id_especialista = models.IntegerField(primary_key=True)
    rut_especialista = models.CharField(max_length = 50 ,verbose_name="rut especialista")
    nombre_especialista = models.CharField(max_length=50,verbose_name="nombre especialista")
    apellido_especialista  = models.CharField(max_length=50,verbose_name="apellido especialista")
    id_especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='id_especialidad',verbose_name="id especialidad")

    class Meta:
        managed = False
        db_table = 'especialista'
            
   
