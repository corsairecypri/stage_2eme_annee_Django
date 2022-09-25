from django.db import models
from django.urls import reverse

class Species(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = 'species'
        

    #L'attribut principal

    species_name = models.CharField(max_length=30)

    def __str__(self):
        return self.species_name


class Researcher(models.Model):

    #Les attributs principaux

    name = models.CharField(max_length=35)
    specialisation = models.CharField(max_length=25)
    labo = models.CharField(max_length=40)

    def __str__(self):
        return self.name



#Les attributs principaux
class ZoneOfStudy(models.Model):

    class Meta:
        verbose_name =  'zone of study'
        verbose_name_plural = 'zones of study'

    #On réalise ici une relation Many to Many entre
    #ZoneOfStudy et Researcher

    researcher = models.ManyToManyField(Researcher)

    name = models.CharField(max_length=30)
    departement = models.CharField(max_length=20)

    commune = models.CharField(max_length=25)
    ecosystem = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class BioSample(models.Model):

    #Le champ de clé primaire permet de créer une relation One to Many
    #entre ZoneOfStudy et BioSample
    #(chaque zone peut posséder plusieurs échantillons mais chaque échantillon
    # est lié à une seule zone)

    zone = models.ForeignKey(ZoneOfStudy, on_delete=models.CASCADE)


    #L'attribut principal (date)

    #L'attribut auto_now_add = True dans un Datefield permet  
    #d'enregistrer la date d'aujourd'hui AU MOMENT DE SA CRéATION
    #(cette donnée ne change plus après)  
    #        
    date = models.DateField()

    #/!\ (Ne doit PAS ETRE CONFONDUE avec auto_now qui permet de 
    # garder en mémoire la date de dernière modification)


    def __str__(self):
        return "%s - %s" %(self.zone, self.date)
        

    #Parfois on a besoin de créer une table intermédiaire
    #spécifique (ici on veut que chaque échantillon possède 
    # plusieurs espèces avec leur nombre de représentants respectifs,
    # mais on veut que la date reste un attribut de BioSample)


    #Comment faire un ManyToMany  avec through

    #sampleData contient le nom du modèle source (ici Species)
    #en 1er paramètre.
    #Puis en 2ème param il stocke le nom de la table intermédiaire dans 'through',
    #Puis enfin dans les 'through_field' le nom du modéle source PUIS du modèle cible...

    sampleData = models.ManyToManyField(
        Species,
        through='SampleData',

        #La table intermédiare stocke les clés primaires (qui sont des 
        # variables venant des throu_fields), ainsi que les attributs
        #qui lui sont propres

        through_fields=('biosample', 'species'),
    )

    #Il faut mettre les même noms de champs (le même nom
    # que pour les pk de la table intermédiaire)



class SampleData(models.Model):
    biosample = models.ForeignKey(BioSample, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    

    number = models.IntegerField()

    def __str__(self):
        return "%s - %s" %(self.species, self.number)

