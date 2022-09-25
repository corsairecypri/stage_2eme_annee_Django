from django.contrib import admin

from .models import Species, Researcher, ZoneOfStudy, BioSample, SampleData


admin.site.register(Species)
admin.site.register(Researcher)
admin.site.register(ZoneOfStudy)


####  Enregistrement du modèle BioSample et de sa table intermédiaire SampleData



#Dans la classe SampleDataInline, on utilise admin.TabularInline
#pour afficher les données d'un objet créé en une seule ligne.

#Avec l'attribut model, on précise qu'on veut afficher les champs 
#du modèle SampleData (la table intermédiaire du modèle BioSample)

#L'attribut extra permet de définir le nombre d'objets créables par défaut
#(On peut librement ajouter ou retirer des objets dans l'administration)

class SampleDataInline(admin.TabularInline):
   model = SampleData
   extra = 4


#La classe BioSampleAdmin utilise ModelAdmin.
#Avec l'attribut inlines, on informe que les données stockées soient 
#celles contenues dans la classe SampleDataInline

class BioSampleAdmin(admin.ModelAdmin):
    inlines = [SampleDataInline]



#En enregistre simultanément BioSample et BioSampleAdmin,
#on ajoute les données de la classe intermédiaire.
#(SampleDataInline stocke les données du modèle SampleData
# et BioSampleAdmin permet de bien les afficher en ligne dans
# l'administration)

#Note : admin.site.register accepte comme 1er paramètre un modèle.
#Comme 2ème param optionnel il accepte une classe d'administration
#(une classe créée avec comme paramètre admin.ModelAdmin, admin.TabularInline ou
# admin.StackedInline)

admin.site.register(BioSample, BioSampleAdmin)


#Note : admin.StackedInline permet d'afficher les attributs d'une classe d'administration
#les uns en dessous des autres (mais ça prend beaucoup de place)

#admin.TabularInline permet d'afficher les attibuts d'une classe administartion sur
#1 seule ligne

