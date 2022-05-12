import json
import jwt
from kafka import KafkaProducer


def send_message_to_kafka(message, message_id, token):
    producer = KafkaProducer(bootstrap_servers=['broker:29092'])
    message_dict = {"message": message, "message_id": message_id, "jwt": token}
    producer.send('quickstart-events', json.dumps(message_dict).encode('utf-8'))
    producer.flush()


def create_jwt_token(message_id):
    encoded_jwt = jwt.encode({"role": "post_message_confirm", "id": message_id}, "n9adta", algorithm="HS256")
    return encoded_jwt
