from django.contrib import admin
from tarefa.models import Task, Tag, Comment, Notification, Attachment
 
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'due_date', 'completed')
    list_filter = ['user', 'completed']
    list_display_links = ('id', 'title',)
    list_editable = ('completed',)
    search_fields = ('title',)
    list_per_page = 10
 
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name' )
    list_display_links = ('id', 'tag_name',)
    search_fields = ('tag_name',)
    list_per_page = 10
 
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_text', 'fk_task', 'created_at')
    list_display_links = ('id', 'comment_text',)
    search_fields = ('comment_text',)
    list_per_page = 10

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_title', 'mini_text', 'notification_user')
    list_display_links = ('notification_title', 'notification_user')
    search_fields = ('notification_title',)
    list_per_page = 10

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('file', 'user_file')
    list_display_links = ('user_file', 'file')
    search_fields = ('user_file',)
    list_per_page = 10
 
admin.site.register(Task, TasksAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Attachment, AttachmentAdmin)