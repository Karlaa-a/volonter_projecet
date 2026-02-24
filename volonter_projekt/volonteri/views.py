from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Aktivnost, Kategorija, Prijava
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.

class ActivityListView(LoginRequiredMixin, ListView): 
    model = Aktivnost 
    template_name = 'aktivnost_list.html'

def index(request):
        return render(request, 'index.html')

class KategorijaListView(LoginRequiredMixin, ListView): 
    model = Kategorija 
    template_name = 'kategorije.html'

class KategorijaDetailView(LoginRequiredMixin, DetailView): 
    model = Kategorija 
    template_name = 'kategorija_detalji.html'
    
class AktivnostDetailView(LoginRequiredMixin, DetailView): 
    model = Aktivnost 
    template_name = 'aktivnost_detalji.html'
    
class PrijavaListView(LoginRequiredMixin, ListView): 
    model = Prijava 
    template_name = 'prijave.html'
    
class PrijavaDetailView(LoginRequiredMixin, DetailView): 
    model = Prijava
    template_name = 'prijava_detalji.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('volonteri:aktivnost_list')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

class AktivnostCreateView(LoginRequiredMixin, CreateView): 
    model = Aktivnost
    fields = ['naziv_aktivnosti', 'opis', 'datum', 'kategorija'] 
    template_name = 'aktivnost_izmjena.html' 
    success_url = reverse_lazy('volonteri:aktivnost_list')
    
class AktivnostUpdateView(LoginRequiredMixin, UpdateView): 
    model = Aktivnost 
    fields = ['naziv_aktivnosti', 'opis', 'datum', 'kategorija'] 
    template_name = 'aktivnost_izmjena.html' 
    success_url = reverse_lazy('volonteri:aktivnost_list') 
        
class AktivnostDeleteView(LoginRequiredMixin, DeleteView): 
    model = Aktivnost 
    template_name = 'aktivnost_brisanje.html' 
    success_url = reverse_lazy('volonteri:aktivnost_list')