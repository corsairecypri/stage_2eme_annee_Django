from django.urls import path

from mybiodata.views import SearcherListView, SearcherCreateView, SearcherUpdateView, SearcherDeleteView, SearcherDetailView
from mybiodata.views import ZoneListView, ZoneCreateView, ZoneUpdateView, ZoneDeleteView, ZoneDetailView
from mybiodata.views import SampleListView, SampleCreateView, SampleUpdateView, SampleDeleteView, SampleDetailView 
from mybiodata.views import createSampleDataView
from mybiodata.views import SpeciesListView, SpeciesCreateView, SpeciesUpdateView, SpeciesDeleteView, SpeciesDetailView

from mybiodata.views import MydataHomePage, MydataCycleData ,MydataCollecte, MydataTraitement, MydataAnalyse, MydataStockage, MydataPartage, MydataReutilisation
from mybiodata.views import MydataRecherche, MydataImportation, MydataVisualisation, MydataTadata

from . import views



urlpatterns = [

    #Les vues des chercheurs

    path('searchers/list/', SearcherListView.as_view(), name="researcher_list"),

    path('searchers/create/', SearcherCreateView.as_view(), name="researcher_create_form"),

    path('searchers/update/<int:pk>/', SearcherUpdateView.as_view(), name="researcher_update_form"),

    path('searchers/delete/<int:pk>/', SearcherDeleteView.as_view(), name="researcher_confirm_delete"),

    path('searchers/detail/<int:pk>/', SearcherDetailView.as_view(), name = "researcher_detail"),


    ## Les vues des zones d'études

    path('zones/list/', ZoneListView.as_view(), name="zoneofstudy_list"),

    path('zones/create/', ZoneCreateView.as_view(), name="zoneofstudy_create_form"),

    path('zones/update/<int:pk>/', ZoneUpdateView.as_view(), name="zoneofstudy_update_form"),

    path('zones/delete/<int:pk>/', ZoneDeleteView.as_view(), name="zoneofstudy_confirm_delete"),

    path('zones/detail/<int:pk>/', ZoneDetailView.as_view(), name = "zoneofstudy_detail"),

    ## Les vues des échantillons

    #   Il reste à régler la CreateView des échantillons

    path('samples/list/', SampleListView.as_view(), name="biosample_list"),

    path('samples/create/', SampleCreateView.as_view(), name="biosample_create_form"),

    #La vue "createSampleDataView" est la vue non générique qui a besoin de l'app_name et
    #se comporte comme une Updateview alors qu'elle est censée être une CreateView

    path('samples/create/<int:pk>', createSampleDataView.as_view(), name = "biosample_create_form"),

    #Cette UpdateView reste à régler car elle n'affiche pas les données comme attendu
    
    path('samples/update/<int:pk>/', SampleUpdateView.as_view(), name="biosample_update_form"),

    path('samples/delete/<int:pk>/', SampleDeleteView.as_view(), name="biosample_confirm_delete"),

    path('samples/detail/<int:pk>/', SampleDetailView.as_view(), name = "biosample_detail"),

    ## Les vues des espèces

    path('species/list/', SpeciesListView.as_view(), name="species_list"),

    path('species/create/', SpeciesCreateView.as_view(), name="species_create_form"),

    path('species/update/<int:pk>/', SpeciesUpdateView.as_view(), name="species_update_form"),

    path('species/delete/<int:pk>/', SpeciesDeleteView.as_view(), name="species_confirm_delete"),

    path('species/detail/<int:pk>/', SpeciesDetailView.as_view(), name = "species_detail"),


    ######### La page d'accueil du site My Data 

    path('mydata/', MydataHomePage.as_view(), name="mydataAccueil"),

    ######### Les vues du site My Data (partie "Comprendre la data")

    path('mydata/cycleData', MydataCycleData.as_view(), name="mydataCycleData"),

    path('mydata/collecte', MydataCollecte.as_view(), name="mydataCollecte"),

    path('mydata/traitement', MydataTraitement.as_view(), name="mydataTraitement"),

    path('mydata/analyse', MydataAnalyse.as_view(), name="mydataAnalyse"),

    path('mydata/stockage', MydataStockage.as_view(), name="mydataStockage"),

    path('mydata/partage', MydataPartage.as_view(), name="mydataPartage"),

    path('mydata/reutilisation', MydataReutilisation.as_view(), name="mydataReutilisation"),

    #Les autres pages du site My Data

    path('mydata/recherche', MydataRecherche.as_view(), name="mydataRecherche"),

    path('mydata/importation', MydataImportation.as_view(), name="mydataImportation"),

    path('mydata/visualisation', MydataVisualisation.as_view(), name="mydataVisualisation"),

    path('mydata/tadata', MydataTadata.as_view(), name="mydataTadata"),


]

#Pour pouvoir utiliser la vue (non-générique) "createSampleDataView", il faut préciser l'app_name
#(ici mybiodata)
app_name = 'mybiodata'

#(Note importante : createSampleDataView est supposée fonctionner comme une CreateView mais elle se comporte 
# de facto comme une UpdateView)