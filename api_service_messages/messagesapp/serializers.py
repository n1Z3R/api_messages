from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from messagesapp.models import MessageModel


class MessageSerializer(ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ('user_id', 'message')
