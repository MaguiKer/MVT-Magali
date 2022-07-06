from django.http import HttpResponse
from django.template import loader,Context,Template
from Familia.models import Personas
import datetime
def mostrar(self):
   familia=[]
  
   persona1=Personas(nombre="Juan",edad=20,fechaNacimiento=datetime.date(2000,1,1))
   persona1.save()
   persona2=Personas(nombre="Pedro",edad=30,fechaNacimiento=datetime.date(2001,1,1))
   persona2.save()
   persona3=Personas(nombre="Maria",edad=40,fechaNacimiento=datetime.date(2002,1,1))
   persona3.save()
   familia=[persona1,persona2,persona3]
   diccionario = {'familia':familia}

   miHtml= open('C:/Users/magui/Downloads/MVT+Magali/plantillas/template.html')
   plantilla = Template(miHtml.read())
   miHtml.close()
   miContexto = Context(diccionario)
   documento= plantilla.render(miContexto)
  
   return HttpResponse(documento)

