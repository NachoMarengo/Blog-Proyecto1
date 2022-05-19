from dataclasses import field
from tkinter import Widget
from django import forms
from models import Comentario

class formularioComentario(forms.ModelForms):
    class Meta:
        model = Comentario 
        field = '__all__'
        Widget = {'fechaComentario': forms.DateInput(attrs={'type': 'date'})}