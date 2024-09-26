from django.contrib import admin
from tarefa.models import Tarefa

# Register your models here.
class Tarefas(admin.ModelAdmin):
    list_display = ('id','name', 
                    'descricao', 
                    'data_inicio',
                    'data_finalizar',
                    'finalizada', 
                    'usuario')
    list_display_links = ('id', 'name')
    list_filter = ('data_inicio',)

admin.site.register(Tarefa, Tarefas)

