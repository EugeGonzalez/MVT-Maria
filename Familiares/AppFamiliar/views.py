from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader
from AppFamiliar.models import Familia

# Create your views here.
def datos(self):
    datos=Familia(integrante="Mamá", nombre="Mari", fecha_nacimiento="1969-02-16")
    datos.save()

    datos_1=Familia(integrante="Papá", nombre="Fer", fecha_nacimiento="1969-02-16")
    datos_1.save()

    datos_2=Familia(integrante="Hija", nombre="Joaquina", fecha_nacimiento="1969-02-16")
    datos_2.save()

    diccionario={'datos':datos, 'datos_1':datos_1, 'datos_2':datos_2}
    

    plantilla=loader.get_template('template.html')

    documento=plantilla.render(diccionario)
    
    return HttpResponse(documento)



    


   

