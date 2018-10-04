from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# categoria = models.ManyToManyField(Categoria, null=True, blank=True)
class Roles (models.Model):
    
    roles = models.CharField(max_length=100)
    def __str__(self):
        return str(self.roles)    
    

class Usuario(models.Model):
   
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100, null=True) 
    codigo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    rol = models.ForeignKey(Roles, on_delete=models.PROTECT) 
    facultad = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.nombre)

class Producto (models.Model):
	nombre 	= models.CharField(max_length=100)
	precio 	= models.IntegerField()
	stock 	= models.IntegerField()
	status 	= models.BooleanField(default=True)
	foto 	= models.ImageField(upload_to='fotos', null=True, blank=True)
	
	# categoria = models.ManyToManyField(Categoria, null=True, blank=True)
	def __str__(self):
		return str(self.nombre)


class Elemento(models.Model):
    UDC = models.CharField(max_length=100, null=True,)
    nombre = models.CharField(max_length=100, null=True,)
    material = models.CharField(max_length=100, null=True,)
    descripcion = models.CharField(max_length=100,null=True,)
    encargado = models.CharField(max_length=100)
    facultad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos',null=True, blank=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.nombre)


   
class Sala(models.Model):
  
    numero= models.IntegerField(null=True) 
    piso = models.IntegerField(null=True) 
    encargado = models.CharField(max_length=100, null=True)
    facultad = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.numero)

class Ip(models.Model):
 
    ip_numero =models.GenericIPAddressField(null=True)
    mascara = models.GenericIPAddressField(null=True)
    asignacion =models.CharField(max_length=100, null=True)
    encargado = models.CharField(max_length=100, null=True)
    facultad = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.ip_numero)
    
  
class Dispositivo (models.Model):
    # id_elemento =  models.IntegerField() 
    nombre = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100, null=True)
    facultad = models.CharField(max_length=100, null=True)
    departamento = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.nombre)

# class Prestamo (models.Model):
#     fecha_inicio= models.DateField(auto_now=False, auto_now_add=False)         
#     fecha_fin= models.DateField(auto_now=False, auto_now_add=False) 
#     id_pre_sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=True) 
#     id_pre_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)  
#     status = models.BooleanField(default=True)
#     def __str__(self):
#         return str(self.id)
   

class PrestamoSala (models.Model):
    fecha_inicio= models.DateField(auto_now=False, auto_now_add=False)         
    fecha_fin= models.DateField(auto_now=False, auto_now_add=False) 
    id_pre_sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=True) 
    id_pre_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)  
    status = models.BooleanField(default=True)
    detalle =  models.CharField(max_length=100, null=True)
    cantidad =  models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id)

class PrestamoIp (models.Model):
    fecha_inicio= models.DateField(auto_now=False, auto_now_add=False)         
    fecha_fin= models.DateField(auto_now=False, auto_now_add=False) 
    id_pre_ip = models.ForeignKey(Ip, on_delete=models.PROTECT, null=True)  
    id_pre_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)  
    status = models.BooleanField(default=True)
    detalle =  models.CharField(max_length=100, null=True)
    cantidad =  models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id)
  
class PrestamoDispositivo (models.Model):
    fecha_inicio= models.DateField(auto_now=False, auto_now_add=False)         
    fecha_fin= models.DateField(auto_now=False, auto_now_add=False) 
    id_pre_disp = models.ForeignKey(Elemento, on_delete=models.PROTECT, null=True) 
    id_pre_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)  
    status = models.BooleanField(default=True)
    detalle =   models.CharField(max_length=100, null=True)
    cantidad =  models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id)




    