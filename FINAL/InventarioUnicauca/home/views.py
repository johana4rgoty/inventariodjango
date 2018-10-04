from django.shortcuts import render,  redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')	
def inicio_view(request):
    return render(request, 'inicio.html', locals())
@login_required(login_url='/login/')	    
def index_view(request):
    return render(request, 'index.html', locals())
def logout_view(request):
    logout(request)
    return redirect('/login/')    
def login_view(request):	
	#return render(request, 'quienes_somos.html', {'n':nombre})
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			user = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username= user, password= cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/index/')
			else:
				msj = 'No se pudo iniciar sesión'   
	formulario=login_form()
	return render(request, 'login.html', locals())
@login_required(login_url='/login/')	    
def quienes_somos_view(request):
	nombre = [12,3,45,67,89,436,51]
	#return render(request, 'quienes_somos.html', {'n':nombre})
	return render(request, 'quienes_somos.html', locals())
# Create your views here.

#**********************************viewtempl*********************************************
@login_required(login_url='/login/')	
def contactenos_view(request):
    email=""
    subject=""
    text=""
    if request.method=='POST':
        formulario = contacto_form(request.POST)
        if formulario.is_valid():
            email     =formulario.cleaned_data['correo']
            subject   =formulario.cleaned_data['asunto']
            text      =formulario.cleaned_data['texto']
            info_enviado = True
            return render (request, 'contactenos.html', locals())
        else:
            msg = 'la informacion es correcta'
    else:
        formulario = contacto_form()

    return render(request,'contactenos.html',locals())
def ver_producto_view(request):    
    return render (request, 'ver_producto.html', locals()) 
def ver_virtual_view(request):    
    return render (request, 'ver_virtual.html', locals()) 
def ver_Salones_view(request):    
    return render (request, 'ver_Salones.html', locals()) 
#def estudiantes_view(request):    
#    return render (request, 'estudiantes.html', locals()) 
#def profesores_view(request):    
#    return render (request, 'profesores.html', locals()) 
def prestamos_view(request):    
    return render (request, 'prestamos.html', locals())             
def informes_view(request):    
    return render (request, 'informes.html', locals()) 
def quienes_somos_view(request):
    return render (request, 'quienes_somos.html', locals())       
def perfil_view(request):    
    return render (request, 'perfil.html', locals()) 
#************************************view_prestamos************************************************     
def lista_sala_view (request):
	lista = Sala.objects.filter()
	return render(request, 'lista_sala.html', locals())
def lista_elemento_view (request):
    lista = Elemento.objects.filter()
    return render(request, 'lista_elemento.html', locals())
def lista_ip_view (request):
    lista = Ip.objects.filter()
    return render(request, 'lista_ip.html', locals())
def lista_usuario_view (request):
    lista = Usuario.objects.filter()
    return render(request, 'lista_usuario.html', locals())   
def lista_admin_view (request):
    lista = User.objects.filter()
    return render(request, 'lista_usu.html', locals())         
 #**********************************************************************************************   

def register_view(request):
	formulario=register_form()

	if request.method == 'POST':
		formulario=register_form(request.POST)
		if formulario.is_valid():

			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u= User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return redirect('/login/')
		else:
			msj= 'no se puedo crear el usuario'

	return render(request, 'register.html', locals())

def thanks_for_register_view(request):
	return render (request, 'register.html', locals())    

def editar_producto_view(request,  id_prod):
    obj= producto.objects.get(id = id_prod)
     #pasar la instancia de ese objeto
    if request.method == 'POST':
        formulario=agregar_producto_form(request.POST, request.FILES, instance=obj)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar_producto/')
            #formulario.save(commit = False)
    formulario=agregar_producto_form(instance=obj)         
    return render(request, 'agregar_producto.html', locals())    

#************************************** agregar*****************************************************************************
def agregar_elemento_view(request): 
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = agregar_elemento_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('/lista_elemento/')
            else:
                msj="hay datos no validos"
        else:
            formulario = agregar_elemento_form()
        return render(request, 'agregar_elemento.html', locals())
    else:
        return redirect('/lista_elemento/')

def agregar_ip_view(request): 
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = agregar_ip_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('/lista_ip/')
            else:
                msj="hay datos no validos"
        else:
            formulario = agregar_ip_form()
        return render(request, 'agregar_ip.html', locals())
    else:
        return redirect('/lista_ip/')

def agregar_sala_view(request): 
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = agregar_sala_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('/lista_sala/')
            else:
                msj="hay datos no validos"
        else:
            formulario = agregar_sala_form()
        return render(request, 'agregar_sala.html', locals())
    else:
        return redirect('/lista_sala/')

def agregar_user_view(request): 
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = agregar_usu_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('/lista_usuario/')
            else:
                msj="hay datos no validos"
        else:
            formulario = agregar_usu_form()
        return render(request, 'agregar_user.html', locals())
    else:
        return redirect('/lista_usuario/')

def agregar_admin_view(request):    

    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = agregar_usuario_form(request.POST, request.FILES)
            if formulario.is_valid():
                usuario = formulario.cleaned_data['username']
                password = formulario.cleaned_data['password']
                u= User.objects.create_user(username=usuario, password=password)
                u.save()           
                # formulario.save()
                return redirect('/lista_usuario/')
            else:
                msj="hay datos no validos"
        else:
            formulario = agregar_usuario_form()
        return render(request, 'agregar_admin.html', locals())
    else:
        return redirect('/lista_usuario/')    	

        
def agregar_profesor_view(request):
    formulario=agregar_profesores_form() 
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = agregar_profesores_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('/principal/')
            else:
                msj="hay datos no validos"
        else:
            formulario = agregar_profesores_form()
        return render(request, 'agregar_profesores.html', locals())
    else:
        return redirect('/principal/')        
           
def agregar_estudiante_view(request): 
    formulario=agregar_estudiante_form()

    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = agregar_estudiante_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()   
                
                return redirect('/principal/')
            else:
                msj="hay datos no validos"
        else:
            formulario = agregar_estudiante_form()
        return render(request, 'agregar_estudiantes.html', locals())
    else:
        return redirect('/principal/') 
          
         
 #********************************************************************************************************               
def ver_producto_view(request, id):
    try:
        obj= Elemento.objects.get(id = id)
    except:
        print("Error en la consulta el Dispositivo no existe")
        msj = "Error en la consulta el Dispositivo no exite"    
    return render(request, 'ver_producto.html', locals())  

def eliminar_producto_view(request,  id):
    obj= Elemento.objects.get(id=id_prod)
     #pasar la instancia de ese objeto
    obj.delete()
    return redirect('listar_producto')

def desactivar_producto_view(request,  id):
    obj= Elemento.objects.get(id=id)
     #pasar la instancia de ese objeto
    obj.delete()
    return redirect('listar_producto')    

#********************************************************************************************************		
def ver_sala_view(request, id):    
    try:
        obj=Sala.objects.get(id=id)
        
    except:
        print ("Error en la consulta el Producto no existe")
        msj = "Error en la consulta el Producto no existe"
    return render(request, 'ver_sala.html', locals())

def eliminar_sala_view (request, id):
	obj = Sala.objects.get(id = id)
	obj.delete()
	return redirect('/lista_sala/')

def desactivar_sala_view(request,  id):
    obj= Sala.objects.get(id=id)
     #pasar la instancia de ese objeto
    obj.status = False
    obj.save()
    return redirect('/lista_sala/')

def editar_sala_view(request,  id):
    obj= Sala.objects.get(id = id)
     #pasar la instancia de ese objeto
    if request.method == 'POST':
        formulario=agregar_sala_form(request.POST, request.FILES, instance=obj)
        if formulario.is_valid():
            formulario.save()
            return redirect('/lista_sala/')
            #formulario.save(commit = False)
    formulario=agregar_sala_form(instance=obj)         
    return render(request, 'agregar_sala.html', locals())        

      
def editar_perfil_view(request,  id):
    obj= Usuario.objects.get(id = id )
    return redirect('/perfil/')
   

 #**************************************************************************
def ver_elemento_view(request, id):    
    try:
        obj=Elemento.objects.get(id=id)
        
    except:
        print ("Error en la consulta el Producto no existe")
        msj = "Error en la consulta el Producto no existe"
    return render(request, 'ver_elemento.html', locals())

def eliminar_elemento_view (request, id):
	obj = Elemento.objects.get(id = id)
	obj.delete()
	return redirect('/lista_elemento/')

def desactivar_elemento_view(request,  id):
    obj= Elemento.objects.get(id=id)
     #pasar la instancia de ese objeto
    obj.status = False
    obj.save()
    return redirect('/lista_elemento/')

def editar_elemento_view(request,  id):
    obj= Elemento.objects.get(id = id)
     #pasar la instancia de ese objeto
    if request.method == 'POST':
        formulario=agregar_elemento_form(request.POST, request.FILES, instance=obj)
        if formulario.is_valid():
            formulario.save()
            return redirect('/lista_elemento/')
            #formulario.save(commit = False)
    formulario=agregar_elemento_form(instance=obj)         
    return render(request, 'agregar_elemento.html', locals())        



#*******************************************************************************

def ver_ip_view(request, id):
    try:
        obj=Ip.objects.get(id=id)       
    except:
        print ("Error en la consulta el Producto no existe")
        msj = "Error en la consulta el Producto no existe"
    return render(request, 'ver_ip.html', locals())

def eliminar_ip_view (request, id):
	obj = Ip.objects.get(id = id)
	obj.delete()
	return redirect('/lista_ip/')

def desactivar_ip_view(request,  id):
    obj= Ip.objects.get(id=id)
     #pasar la instancia de ese objeto
    obj.status = False
    obj.save()
    return redirect('/lista_ip/')

def editar_ip_view(request,  id):
    obj= Ip.objects.get(id = id)
     #pasar la instancia de ese objeto
    if request.method == 'POST':
        formulario=agregar_ip_form(request.POST, request.FILES, instance=obj)
        if formulario.is_valid():
            formulario.save()
            return redirect('/lista_ip/')
            #formulario.save(commit = False)
    formulario=agregar_ip_form(instance=obj)         
    return render(request, 'agregar_ip.html', locals())        

  
  #************************************************************************************
def ver_usuario_view(request, id):    
    try:
        obj=Usuario.objects.get(id=id)       
    except:
        print ("Error en la consulta el Producto no existe")
        msj = "Error en la consulta el Producto no existe"
    return render(request, 'ver_usuario.html', locals())

def eliminar_usuario_view (request, id):
	obj = Usuario.objects.get(id = id)
	obj.delete()
	return redirect('/lista_usuario/')

    
def desactivar_usuario_view(request,  id):
    obj= Usuario.objects.get(id=id)
     #pasar la instancia de ese objeto
    obj.status = False
    obj.save()
    return redirect('/lista_usuario/')

def editar_usuario_view(request,  id):
    obj= Usuario.objects.get(id = id)
     #pasar la instancia de ese objeto
    if request.method == 'POST':
        formulario=agregar_usu_form(request.POST, request.FILES, instance=obj)
        if formulario.is_valid():
            formulario.save()
            return redirect('/lista_usuario/')
            #formulario.save(commit = False)
    formulario=agregar_usu_form(instance=obj)         
    return render(request, 'agregar_user.html', locals())   

#******************************************************************************************************************************
#                                               PRESTAMOS
#******************************************************************************************************************************

def prestamosDispositivos_view(request):
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = Prestamo_Dispositivo_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('/index/')

            else:
                msj="hay datos no validos"
        else:
            formulario = Prestamo_Dispositivo_form()
        return render(request, 'prestamosDispositivos.html', locals())
    else:
        return redirect('/index/')  

  

def prestamosIp_view(request): 
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = Prestamo_Ip_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('/index/')
            else:
                msj="hay datos no validos"
        else:
            formulario = Prestamo_Ip_form()
        return render(request, 'agregar_usuario.html', locals())
    else:
        return redirect('/index/')  

def prestamosSalones_view(request): 
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = Prestamo_Salon_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('/index/')
            else:
                msj="hay datos no validos"
        else:
            formulario = Prestamo_Salon_form()
        return render(request, 'prestamosSalones.html', locals())
    else:
        return redirect('/index/')                  
