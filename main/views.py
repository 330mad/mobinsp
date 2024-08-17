from django.shortcuts import render, redirect
from .models import InspDetDOT, VoilByDOT
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView



class dotformUpdateView(UpdateView):
    model = InspDetDOT
    template_name = 'main/dotform_create.html'
    form_class = InspDetDOTForm
class dotformDeleteView(DeleteView):
    model = InspDetDOT
    success_url = '/about/form'
    template_name = 'main/dotform_delete.html'

class by_dotUpdateView(UpdateView):
    model = VoilByDOT
    template_name = 'main/by_DOT_create.html'
    form_class = VoilByDOTForm
    context_object_name = 'voilbydot'
    success_url = reverse_lazy('byDOT')
class by_dotDeleteView(DeleteView):
    model = VoilByDOT
    success_url = '/about/bydot'
    template_name = 'main/by_DOT_delete.html'

#---------------------------------------------------------------------------
def MainMain(request):
    return render(request, 'main/MainMain.html')

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

#-------------------------------------------------------------------------------------------
def dotform(request):
    dot_form = InspDetDOT.objects.all()
    return render(request, 'main/dotform.html', {'dot_form': dot_form})

def dotform_create(request):
    error = ''
    if request.method == 'POST':
        form = InspDetDOTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('DOTform')
        else:
            error = 'Форма заполнена невернo!'

    form = InspDetDOTForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/dotform_create.html', data)

#-------------------------------------------------------------------------------------------
def by_DOT(request):
    by_dot = VoilByDOT.objects.all()
    return render(request, 'main/by_DOT.html', {'by_dot': by_dot})

def by_DOT_create(request):
    error = ''
    if request.method == 'POST':
        form = VoilByDOTForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('byDOT')
        else:
            error = 'Форма заполнена невернo!'

    form = VoilByDOTForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/by_DOT_create.html', data)









def out_dot(req):
    return render(req, 'main/out_DOT.html')

def last_dot(req):
    return render(req, 'main/last_DOT.html')

def check_svtk(req):
    return render(req, 'main/check_SVTK.html')

def svtkform(req):
    return render(req, 'main/SVTKform.html')

def svtkprogcheck(req):
    return render(req, 'main/SVTK_progcheck.html')

def stat(req):
    return render(req, 'main/stat.html')