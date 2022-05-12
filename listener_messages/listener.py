import json
import jwt
import requests
from kafka import KafkaConsumer

BANWORD = "АБРАКАДАБРА"


def send_post_message_confirmation(message_id, success):
    url = 'http://web:8000/api/v1/message_confirmation'
    data = {'message_id': f'{message_id}', 'success': success}
    requests.post(url, data=data)
    print(data)


def message_confirmation(message: dict):
    message_content = message.get("message").lower()
    if BANWORD.lower() in message_content:
        send_post_message_confirmation(message.get("message_id"), False)
    else:
        send_post_message_confirmation(message.get("message_id"), True)


def token_validate(message: dict):
    token = jwt.encode({"role": "post_message_confirm", "id": message["message_id"]}, "n9adta", algorithm="HS256")
    if token == message.get("jwt"):
        message_confirmation(message)


consumer = KafkaConsumer('quickstart-events', bootstrap_servers="broker:29092")
for msg in consumer:
    token_validate(json.loads(msg.value.decode('utf-8')))
