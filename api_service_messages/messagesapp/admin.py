from django.contrib import admin

# Register your models here.
from messagesapp.models import MessageModel

admin.site.register(MessageModel)
