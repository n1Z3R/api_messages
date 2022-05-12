from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from messagesapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/message', MessageCreateAPI.as_view()),
    path('api/v1/message_confirmation', MessageConfirmation.as_view())
]
