from .models import Articulo
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    referencias = Articulo.objects.all()
    template = loader.get_template('inventario/index.html')
    context = {
        'referencias': referencias,
    }
    return HttpResponse(template.render(context, request))
