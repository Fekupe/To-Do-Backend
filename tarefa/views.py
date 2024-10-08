from django.http import JsonResponse
from rest_framework import viewsets, generics
from tarefa.models import Task, Tag, Comment, Notification, Attachment
from tarefa.serializer import TarefaSerializers, TagSerializers, CommentSerializers, NotificationSerializers, AttachmentSerializers, ListCommentSerializers, ListTagSerializers

# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TarefaSerializers

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all
    serializer_class = TagSerializers

class ListTagViewSets(generics.ListAPIView):
    def get_queryset(self):
        queryset = Tag.objects.filter(tasks__in=[self.kwargs['pk']])
        return queryset
    serializer_class = ListTagSerializers

class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all
    serializer_class = CommentSerializers

class ListCommentsViewSets(generics.ListAPIView):
    def get_queryset(self):
        queryset = Comment.objects.filter(fk_user=self.kwargs['pk'])
        return queryset
    serializer_class = ListCommentSerializers

class NotificationViewSets(viewsets.ModelViewSet):
    queryset = Notification.objects.all
    serializer_class = NotificationSerializers

class AttachmentViewSets(viewsets.ModelViewSet):
    queryset = Attachment.objects.all
    serializer_class = AttachmentSerializers