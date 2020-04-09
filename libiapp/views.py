from django.shortcuts import render

# Create your views here.

from .models import Socio,Provincia,Municipio,Incidencia

def index(request):
    """
    Función vista para la página inicio del sitio
    """
    # Genera contadores de algunos de los objetos principales
    num_socios=Socio.objects.all().count()
    num_socios_alta=Socio.objects.filter(fecha_baja__isnull=True).count()
    num_socios_baja=Socio.objects.filter(fecha_baja__isnull=False).count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto 
    return render(
        request,
        'index.html',
        context={'num_socios':num_socios,'num_socios_alta':num_socios_alta,'num_socios_baja':num_socios_baja},
    )

from django.views import generic

class SocioListView(generic.ListView):
    model=Socio
    paginate_by = 10

class SocioDetailView(generic.DetailView):
    model=Socio

class IncidenciaListView(generic.ListView):
    model=Incidencia

class IncidenciaDetailView(generic.DetailView):
    model=Incidencia

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Socio

#class SocioCreate(PermissionRequiredMixin,CreateView):
class SocioCreate(CreateView):
    model = Socio
    fields = '__all__'
#   initial={'nombre_del_campo':'Valor Inicial'}
#   Permission_required

class SocioUpdate(UpdateView):
    model = Socio
    fields = '__all__'
#   fields = ['campo1', 'campo2',...]

class SocioDelete(DeleteView):
    model = Socio
    success_url = reverse_lazy('socios')
