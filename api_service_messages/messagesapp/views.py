from django.forms import model_to_dict
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from messagesapp.models import MessageModel
from messagesapp.serializers import MessageSerializer
from messagesapp.services import send_message_to_kafka, create_jwt_token


class MessageCreateAPI(CreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        send_message_to_kafka(obj.message, obj.id, create_jwt_token(obj.id))


class MessageConfirmation(APIView):
    def post(self, request):
        if request.data["success"] == 'True':
            message = MessageModel.objects.get(pk=request.data["message_id"])
            message.status = "c"
            message.save()
        elif request.data["success"] == 'False':
            message = MessageModel.objects.get(pk=request.data["message_id"])
            message.status = "b"
            message.save()
        return Response(model_to_dict(message))
