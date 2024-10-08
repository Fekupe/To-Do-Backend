from tarefa.models import Task, Tag, Comment, Notification, Attachment
from rest_framework import serializers

class TarefaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ListTagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tasks', 'tag_name']

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ListCommentSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Comment 
        fields = ['fk_user', 'comment_text', 'fk_task'] 
	

class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class AttachmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'