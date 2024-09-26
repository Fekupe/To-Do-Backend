from django.http import JsonResponse
from rest_framework import viewsets
from tarefa.models import Tarefa
from serializer import TarefaSerializers

# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
	'''Exibir todas as tarefas'''
	query = Tarefa.objects.all()
	Serializer_class = TarefaSerializers

	#queryset = Music.objects.get(pk='')   #Coloque o ID que deseja retornar
	#queryset = Tarefa.objects.value_list('id', flat=True)