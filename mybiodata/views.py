from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from mybiodata.models import BioSample, Researcher, ZoneOfStudy, Species, SampleData

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.list import ListView 


from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy, reverse

from .forms import BioSampleDataFormset

from django.forms import inlineformset_factory

from django.contrib import messages


#La page d'accuel du site My Data 

class MydataHomePage(TemplateView):

    template_name = "mybiodata/mydataAccueil.html"


#Les TemplateViews du site My Data (partie "Comprendre la data")

class MydataCycleData(TemplateView):

    template_name = "mybiodata/mydataCycleData.html"

class MydataCollecte(TemplateView):

    template_name = "mybiodata/mydataCollecte.html"

class MydataTraitement(TemplateView):

    template_name = "mybiodata/mydataTraitement.html"

class MydataAnalyse(TemplateView):

    template_name = "mybiodata/mydataAnalyse.html"

class MydataStockage(TemplateView):

    template_name = "mybiodata/mydataStockage.html"

class MydataPartage(TemplateView):

    template_name = "mybiodata/mydataPartage.html"

class MydataReutilisation(TemplateView):

    template_name = "mybiodata/mydataReutilisation.html"


#Les autres pages du site My data

class MydataRecherche(TemplateView):

    template_name = "mybiodata/mydataRecherche.html"

class MydataImportation(TemplateView):

    template_name = "mybiodata/mydataImportation.html"

class MydataVisualisation(TemplateView):

    template_name = "mybiodata/mydataVisualisation.html"

class MydataTadata(TemplateView):

    template_name = "mybiodata/mydataTadata.html"



######Les vues dépendant des modèles

## Les vues des chercheurs

class SearcherListView(ListView) :

    model = Researcher


class SearcherCreateView(CreateView):
    model = Researcher
    fields = ['name', 'specialisation', 'labo']

    template_name_suffix = '_create_form'


class SearcherUpdateView(UpdateView):
    model = Researcher
    fields = ['name', 'specialisation', 'labo']

    template_name_suffix = '_update_form'


class SearcherDeleteView(DeleteView):
    model = Researcher
    success_url = reverse_lazy('researcher_list')

class SearcherDetailView(DetailView):

    model = Researcher


## Les vues des zones

class ZoneListView(ListView) :

    model = ZoneOfStudy


class ZoneCreateView(CreateView):
    model = ZoneOfStudy
    fields = ['name', 'departement', 'commune', 'ecosystem']

    template_name_suffix = '_create_form'

class ZoneUpdateView(UpdateView):
    model = ZoneOfStudy
    fields = ['name', 'departement', 'commune', 'ecosystem']

    template_name_suffix = '_update_form'

class ZoneDeleteView(DeleteView):
    model = ZoneOfStudy
    success_url = reverse_lazy('zoneofstudy_list')

class ZoneDetailView(DetailView):

    model = ZoneOfStudy

## Les vues des échantillons

class SampleListView(ListView):

    model = BioSample


class SampleCreateView(CreateView):
    model = BioSample
    fields = ['zone', 'date', 'sampleData']             #"Marche" mais n'affiche que les espèces et pas leur nombre
    #fields = ['zone', 'date', 'species', 'number']     #Ne marche pas mais j'aurai essayé

    #fields = ['zone', 'date'] 

    template_name_suffix = '_create_form'


###################################################################################

#J'ai essayé de mettre CreateView à la place de FormView après
#SingleObjectMixin mais ça n'a pas marché.
class createSampleDataView(SingleObjectMixin, FormView):

    model = BioSample
    template_name = 'mybiodata/gabaritCreateSampleDataView.html'

    #Cette fonction doit retourner un objet BioSample
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset = BioSample.objects.all())
        return super().get(request, *args, **kwargs)
    
    #Cette fonction permet de poster un objet BioSample
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset = BioSample.objects.all())
        return super().post(request, *args, **kwargs)

    #Le formulaire BioSampleDataFormset a été codé dans forms.py
    def get_form(self, form_class=None):
        return BioSampleDataFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        #add_message a besoin d'un import spécial pour fonctionner
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved'
        )

        return HttpResponseRedirect(self.get_success_url())

    #Dans cette fonction, reverse cherche l'app_name mybiodata, puis le gabarit de
    #la DetailView des échantillons
    def get_success_url(self):
        return reverse('mybiodata:biosample_detail', kwargs={'pk': self.object.pk})
    

#Voir la vidéo suivante à partir de 1:03:25  pour la partie la plus importante
# https://www.youtube.com/watch?v=OduVfuv44K8 

#Mais n'oubliez pas de voir la partie sur les URLs au tout début (car le get_success_url
# à la fin a besoin de trouver un app_name dans le urls.py)

###################################################################################

class SampleUpdateView(CreateView):
    model = BioSample
    fields = ['zone', 'date', 'sampleData']

    template_name_suffix = '_update_form'

class SampleDeleteView(DeleteView):
    model = BioSample
    success_url = reverse_lazy('zoneofstudy_list')

class SampleDetailView(DetailView):

    model = BioSample

## Les vues des espèces

class SpeciesListView(ListView) :

    model = Species


class SpeciesCreateView(CreateView):
    model = Species
    fields = ['species_name']

    template_name_suffix = '_create_form'

class SpeciesUpdateView(UpdateView):
    model = Species
    fields = ['species_name']

    template_name_suffix = '_create_form'

class SpeciesDeleteView(DeleteView):
    model = Species
    success_url = reverse_lazy('species_list')

class SpeciesDetailView(DetailView):

    model = Species