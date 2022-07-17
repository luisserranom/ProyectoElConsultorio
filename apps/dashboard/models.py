from django.db import models

# Create your models here.
class Rango(models.Model):
    id_rango = models.AutoField(primary_key=True)
    rango = models.CharField(max_length= 1)

    def __str__(self):
        return  '{}'.format(self.id_rango)  
    
    class Meta:
        managed = False
        db_table = 'rango'
        
class Paciente(models.Model):
    id_paciente  = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50 ,verbose_name="Nombre")
    Papellido = models.CharField(max_length=50,verbose_name="Apellido paterno")
    Sapellido = models.CharField(max_length=50,verbose_name="Apellido materno",null=True)
    rut  = models.CharField(max_length=50,verbose_name="rut especialista")
    correo = models.EmailField(max_length=50)
    id_rango = models.ForeignKey(Rango, models.DO_NOTHING, db_column='id_rango',verbose_name=" id_rango")
   
    def nombre_completo(self):
        return "{} {} {}".format(self.nombre,self.Papellido,self.Sapellido)     
    
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        managed = False
        db_table = 'paciente'

        
class Area(models.Model):
    id_area  = models.AutoField(primary_key = True)
    nombre_area = models.CharField(max_length = 50 ,verbose_name="Nombre area")
    
    class Meta:
        managed = False
        db_table = 'Area' 
        
    def __str__(self):
        return '{}'.format(self.nombre_area)

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
    
    
    def nombre_completo_esp(self):
        return "{} {}".format(self.nombre_especialista,self.apellido_especialista)     
    
    def __str__(self):
        return self.nombre_completo_esp()
   
class Hora(models.Model):
    id_hora = models.AutoField(primary_key=True)
    fecha = models.DateField()  
    hora = models.TimeField()
    estado = models.CharField(max_length=50)
    id_especialista = models.ForeignKey(Especialista, models.DO_NOTHING, db_column='id_especialista',verbose_name="id especialista")
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='id_area',verbose_name="id Area")
    class Meta:
        managed = False
        db_table = 'hora'   
     
    def __str__(self):
        return '{}'.format(self.id_hora)
    
class RegistroHora(models.Model):
    id_registro  = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=50,verbose_name="Descripcion hora medica")
    fecha = models.DateField()
    hora = models.TimeField(blank=True)
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='id_paciente',verbose_name="id paciente")
    id_hora = models.ForeignKey(Hora, models.DO_NOTHING, db_column='id_hora',verbose_name="id hora")
    class Meta:
        managed = False
        db_table = 'RegistroHora' 
        
    def __str__(self):
        return '{}'.format(self.id_registro)

class ListaSolicitudHora(models.Model):
    
    id_solicitud = models.AutoField(primary_key=True,verbose_name="id especialidad")
    descripcion = models.CharField(max_length=300,verbose_name="descripcion")
    hora = models.TimeField(blank=True)
    fecha = models.DateField()
    respuesta = models.CharField(max_length=200)
    estado = models.CharField(max_length=30)
    id_registro = models.ForeignKey(RegistroHora, models.DO_NOTHING, db_column='id_registro',verbose_name="id registro")
    
    class Meta:
        managed = False
        db_table = 'listaSolicitud'
        
        
    def __str__(self):
        return '{}'.format(self.id_solicitud)