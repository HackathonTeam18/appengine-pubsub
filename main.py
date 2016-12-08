from flask import Flask, request, jsonify
from pubsub import PubSub
import json
import base64


app = Flask(__name__)
pubsub_client = PubSub()


@app.route('/')
def hello_world():
    """hello world"""
    return 'Hello World!'


'''Create topic'''
@app.route('/pubsub/receive', methods=['POST'])
def pubsub_create_topic():
    obj = request.get_json()
    print json.dumps(obj)
    topic_name = obj['name']
    topic = pubsub_client.create_topic(topic_name)
    data = 'Topic {} created.'.format(topic.name)
    return jsonify(data), 200


'''List topics'''
@app.route('/pubsub/receive', methods=['GET'])
def pubsub_list_topics():
    topics = pubsub_client.list_topics()
    return jsonify(topics), 200


@app.route('/pubsub/receive/<topic_name>', methods=['DELETE'])
def pubsub_delete_topic(topic_name):
    pubsub_client.delete_topic(topic_name)
    return jsonify('Topic {} deleted.'.format(topic_name)), 200


if __name__ == '__main__':
    # Used for running locally
    app.run(host='127.0.0.1', port=8080, debug=True)
