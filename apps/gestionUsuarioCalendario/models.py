from django.db import models

# Create your models here.
class Remedio(models.Model):
    id_remedio = models.AutoField(primary_key=True)
    nombre_remedio = models.CharField(max_length = 50)
    class Meta:
        managed = False
        db_table = 'remedio' 

    def __str__(self):
        return '{}'.format(self.nombre_remedio)



class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    indicaciones = models.CharField(max_length=100)
    fecha_Retiro = models.DateField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=30)
    respuesta = models.CharField(max_length=100,blank=True,null=True)
    id_remedio = models.ForeignKey(Remedio, models.DO_NOTHING, db_column='id_remedio',verbose_name="id remedio")
    class Meta:
        managed = False
        db_table = 'receta' 

    def __str__(self):
        return '{}'.format(self.id_receta, self.indicaciones, self.fecha_Retiro, self.fecha_limite, self.estado)  
    
    
class EnfermedadesCronicas(models.Model):
    id_enfermedades_cronicas = models.AutoField(primary_key = True)
    nombre_enfermedad = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.nombre_enfermedad)  
        
    class Meta:
        managed = False
        db_table='enfermedadesCronica'


class Alergias(models.Model):
    id_alergias = models.AutoField(primary_key = True)
    nombre_alergia = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.nombre_alergia, self.this)  
        
    class Meta:
        managed = False
        db_table='alergias'
        
class EnfermedadesTerminales(models.Model):
    id_enfermedades_terminales = models.AutoField(primary_key = True)
    nombre_enfermedad_terminal = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.nombre_enfermedad_terminal)  
        
    class Meta:
        managed = False
        db_table='enfermedadesTerminales'
        
        
class Observaciones(models.Model):
    id_observacion = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()
    
    def __str__(self):
        return '{}'.format(self.id_observacion)  
        
    class Meta:
        managed = False
        db_table='enfermedadTerminal'
        
        
        
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
      
    
    def __str__(self):
        return  '{}'.format(self.nombre)  
    
    class Meta:
        managed = False
        db_table = 'paciente' 
         
        
class FichaMedica(models.Model):
    id_ficha = models.AutoField(primary_key = True)
    id_receta = models.ForeignKey(Receta, models.DO_NOTHING, db_column='id_receta',verbose_name="id receta",null = True, blank=True)
    id_enfermedades_cronicas = models.ForeignKey(EnfermedadesCronicas, models.DO_NOTHING, db_column='id_enfermedades_cronicas',verbose_name="id enfermedades cronicas",null = True, blank=True)
    id_alergias = models.ForeignKey(Alergias, models.DO_NOTHING, db_column='id_alergias',verbose_name="id alergias",null = True, blank=True)
    id_enfermedades_terminales = models.ForeignKey(EnfermedadesTerminales, models.DO_NOTHING, db_column='id_enfermedades_terminales',verbose_name="id enfermedades terminales",null = True, blank=True)
    id_observacion = models.ForeignKey(Observaciones, models.DO_NOTHING, db_column='id_observacion',verbose_name="id observacion",null = True, blank=True)
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='id_paciente',verbose_name="id paciente")
    def __str__(self):
        return '{}'.format(self.id_ficha)  
        
    class Meta:
        managed = False
        db_table='fichaMedica'