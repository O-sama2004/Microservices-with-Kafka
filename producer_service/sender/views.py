from django.shortcuts import render

from django.http import JsonResponse
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_message(request):
    data = {"message": "Hello from producer!"}
    producer.send('test-topic', value=data)
    return JsonResponse({"status": "message sent"})