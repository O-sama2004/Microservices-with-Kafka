from django.shortcuts import render

from django.http import JsonResponse
from kafka import KafkaProducer
import json

def send_message(request):
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        data = {"message": "Hello from producer!"}
        producer.send('test-topic', value=data)
        producer.flush()  # ensure message is sent
        return JsonResponse({"status": "message sent"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)