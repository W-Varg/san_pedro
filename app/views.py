from django.views.generic import TemplateView
#from django_ajax.mixin import AJAXMixin
from django.shortcuts import render
import winsound
import pandas as pd
import xlsxwriter

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)
def alarma(frecuencia, duracion):
    winsound.Beep(frecuencia,duracion)

from .models import *

def exportar(arreglo):
    mylist = list(arreglo)
    #print("[{0}]".format(', '.join(map(str, mylist))))
    # Create a Pandas dataframe from some data.
    df = pd.DataFrame({'Data': mylist})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

class IndexView(TemplateView):
    template_name = "base.html"

    def post(self, request, *args, **kwargs):
        code = request.POST['code']
        msg = ''
        status = False
        id_tarjeta = Tarjeta.objects.filter(number=code).values_list('id', flat=True)
        if id_tarjeta:
            id_usuario = Persona.objects.filter(tarjetas_id=id_tarjeta[0]).values_list('id', flat=True)
            
            if id_usuario:
                registro = Registry()
                registro.user_name = Persona.objects.get(pk=id_usuario[0])
                registro.tarjeta = code
                registro.save()
                msg = 'Registro Exitoso: '+code
                alarma(2300,1000)
                status = True
                
            else:
                msg = 'No hay usuario para esta tarjeta: '+code
                alarma(2300,100)
                alarma(2320,100)
        else: 
            msg = 'Numero de tarjeta no encontrado'
            alarma(2300,500)
        
        list_r = Registry.objects.prefetch_related('user_name').order_by('-date_registry')[:5]
        list_total = Registry.objects.count()

        exportar(list_r)
        
        context = {'msm' : msg, 'list_register': list_r, 'st':status, 'total':list_total}
        return render(request,'base.html',context)