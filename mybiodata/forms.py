from django import forms
from django.forms import inlineformset_factory

from .models import BioSample, SampleData, Species

BioSampleDataFormset = inlineformset_factory(BioSample, SampleData, fields=('species', 'number'))

