from django import forms
from .models import *
import datetime
from django.db import models



class contacto_form (forms.Form):
    correo = forms.EmailField(widget=forms.TextInput())
    asunto = forms.CharField(widget=forms.TextInput())
    texto = forms.CharField(widget=forms.Textarea())


class login_form (forms.Form):
#	widget={
#		'usuario':forms.TextInput(attrs={'class':'form-control'}),
#		'clave'  :forms.PasswordInput(attrs={'class':'form-control'}),
#	}
	usuario =  forms.CharField ( widget=forms.TextInput(attrs={'class':'form-control'}))
	clave   =  forms.CharField (widget=forms.PasswordInput(attrs={'class':'form-control'}, render_value=False))

class register_form(forms.Form):
	userName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password_1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'},render_value=False))
	password_2 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput(attrs={'class':'form-control'},render_value=False))


	def clean_username(self):
		userName=self.cleaned_data['username']
		try:
			u=User.objects.get(username= username)
		except User.DoesNotExist:
			return username
			raise forms.ValidationError('Nombre de usuario ya registrado')
	
	def clean_email(self):
		email=self.cleaned_data['email']

		try:
			email=User.objects.get(email=email)

		except User.DoesNotExist:
			return email

		raise forms.ValidationError('Correo electrónico ya existe')

	def clean_password_2(self):
		password_1=self.cleaned_data['password_1']
		password_2=self.cleaned_data['password_2']

		if password_1==password_2:
			pass
		else:
			raise forms.ValidationError('Contraseñas no coinciden')

class Registro_form(forms.Form):
	id_cedula =  forms.CharField ( widget=forms.TextInput(attrs={'class':'form-control'}))
	nombre_apellido =  forms.CharField ( widget=forms.TextInput(attrs={'class':'form-control'}))
	codigo =  forms.CharField ( widget=forms.TextInput(attrs={'class':'form-control'}))
	telefono =  forms.CharField ( widget=forms.TextInput(attrs={'class':'form-control'}))
	rol =  forms.CharField ( widget=forms.TextInput(attrs={'class':'form-control'}))
	
	
class agregar_sala_form (forms.ModelForm):
	class Meta:
		model  = Sala 
		fields = '__all__'
		widgets= {
			'numero':forms.TextInput(attrs={'class':'form-control'}), 
			'piso':forms.TextInput(attrs={'class':'form-control'}), 
			'encargado':forms.TextInput(attrs={'class':'form-control'}), 
			'facultad':forms.TextInput(attrs={'class':'form-control'}), 		
					}
		labels = {
			'status':'Disponible', 
		}

class editar_perfil_form (forms.ModelForm):
	class Meta:
		model  = Usuario 
		fields = '__all__'
		widgets= {
			
			'id_cedula':forms.TextInput(attrs={'class':'form-control'}), 
			'encargado':forms.TextInput(attrs={'class':'form-control'}), 
			'facultad':forms.TextInput(attrs={'class':'form-control'}), 
						
			

		}
		labels = {
			'status':'Disponible', 
		}


class agregar_ip_form (forms.ModelForm):
	class Meta:
		model  = Ip 
		fields = '__all__'
		widgets= {
			
			'ip_numero':forms.TextInput(attrs={'class':'form-control'}), 
			'mascara':forms.TextInput(attrs={'class':'form-control'}), 
			'asignacion':forms.TextInput(attrs={'class':'form-control'}), 
			'encargado':forms.TextInput(attrs={'class':'form-control'}), 
			'facultad':forms.TextInput(attrs={'class':'form-control'}), 
					
					}
		labels = {
			'status':'Disponible', 
		}		



class agregar_elemento_form (forms.ModelForm):
	class Meta:
		model  = Elemento 
		fields = '__all__'
		widgets= {
			'UDC':forms.TextInput(attrs={'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'class':'form-control'}), 
			'material':forms.TextInput(attrs={'class':'form-control'}), 			
			'encargado':forms.TextInput(attrs={'class':'form-control'}), 
			'descripcion':forms.TextInput(attrs={'class':'form-control'}), 
			'facultad':forms.TextInput(attrs={'class':'form-control'}), 
			'departamento':forms.TextInput(attrs={'class':'form-control'}), 
	    		
					}
		labels = {
			'status':'Disponible', 
		}		

class agregar_estudiante_form(forms.ModelForm):
	class Meta:
		model  = Usuario 
		fields = '__all__'
		widgets= {
			
			'id_cedula':forms.TextInput(attrs={'class':'form-control'}), 
			'nombre':forms.TextInput(attrs={'class':'form-control'}), 
			'codigo':forms.TextInput(attrs={'class':'form-control'}), 
			'telefono':forms.TextInput(attrs={'class':'form-control'}), 
			'rol':forms.TextInput(attrs={'class':'form-control', 'disabled':'True',   'value': '1'} ), 
			'facultad':forms.TextInput(attrs={'class':'form-control'}),			 	
					}
		labels = {
			'status':'Disponible', 
		}

class agregar_usu_form(forms.ModelForm):
	class Meta:
		model  = Usuario 
		fields = '__all__'
		widgets= {
			
			'id_cedula':forms.TextInput(attrs={'class':'form-control'}), 
			'nombre':forms.TextInput(attrs={'class':'form-control'}), 
			'codigo':forms.TextInput(attrs={'class':'form-control'}), 
			'cedula':forms.TextInput(attrs={'class':'form-control'}), 
			'telefono':forms.TextInput(attrs={'class':'form-control'}),		
			'facultad':forms.TextInput(attrs={'class':'form-control'}),			 	
					}
		labels = {
			'status':'Disponible', 
		}
	

class agregar_profesores_form(forms.ModelForm):
	class Meta:
		model  = Usuario 
		fields = '__all__'
		widgets= {
			
			'id_cedula':forms.TextInput(attrs={'class':'form-control'}), 
			'nombre':forms.TextInput(attrs={'class':'form-control'}), 
			'codigo':forms.TextInput(attrs={'class':'form-control'}), 
			'telefono':forms.TextInput(attrs={'class':'form-control'}), 
			'rol':forms.TextInput(attrs={'class':'form-control', 'disabled':'True',   'value': '1'} ), 
			'facultad':forms.TextInput(attrs={'class':'form-control'}),			 	
					}
		labels = {
			'status':'Disponible', 
		}			

class agregar_usuario_form(forms.ModelForm):
	class Meta:
		model= User
		fields = [
			'last_name',
			'first_name',
			'email',
			'username',
			'password',		
			
		]
		widgets = {
			'last_name':forms.TextInput(attrs={'class':'form-control'}), 
			'first_name':forms.TextInput(attrs={'class':'form-control'}), 
			'email':forms.TextInput(attrs={'class':'form-control'}), 
			'username':forms.TextInput(attrs={'class':'form-control'}), 
			'password': forms.PasswordInput(attrs={'class':'form-control'},render_value=False)
		}
		
		


class Prestamo_Salon_form(forms.ModelForm):
	class Meta:
		model  = PrestamoSala 
		fields = '__all__'
		widgets= {
			
			'id_informe':forms.TextInput(attrs={'class':'form-control'}), 
			'fecha_inicio':forms.TextInput(attrs={'type':'date', 'class':'form-control'}), 
			'fecha_fin':forms.TextInput(attrs={'type':'date', 'class':'form-control'}), 
							 	
					}
		labels = {
			'status':'Disponible', 
		}

class Prestamo_Dispositivo_form(forms.ModelForm):
	class Meta:
		model  = PrestamoDispositivo 
		fields = '__all__'
		widgets= {
			
			'id_informe':forms.TextInput(attrs={'class':'form-control'}), 
			'fecha_inicio':forms.TextInput(attrs={'type':'date', 'class':'form-control'}), 
			'fecha_fin':forms.TextInput(attrs={'type':'date', 'class':'form-control'}), 
					}
		labels = {
			'status':'Disponible', 
		}
class Prestamo_Ip_form(forms.ModelForm):
	class Meta:
		model  = PrestamoIp 
		fields = '__all__'
		widgets= {
			
			'id_informe':forms.TextInput(attrs={'class':'form-control'}), 
			'fecha_inicio':forms.TextInput(attrs={'type':'date', 'class':'form-control'}), 
			'fecha_fin':forms.TextInput(attrs={'type':'date', 'class':'form-control'}), 
					}
		labels = {
			'status':'Disponible', 
		}
