import pika
import uuid
from flask import Flask, jsonify

app = (__name__)

def send_snap(url):
    data = []
    uid = uuid.uuid1()
    data.append ({'url': url, 'uuid': uid})
    data_body = jsonify(data)
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='shotta_snap')
        channel.basic_publish(exchange='',routing_key='shoota_snap', body=data_body)
        return { "shot_id" : uid }
    except Exception as e:
        return { "error" : "Shotta appears to have encountered an issues. Try again." }
    
@app.route('/')
def index():
    return { "status" : "online" }

@app.route('/shotta')
def shotit(url):
    return send_snap(url) #Send it to the mqueue

