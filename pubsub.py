from google.cloud import pubsub


class PubSub:


    def __init__(self):
        self.pubsub_client = pubsub.Client()

    
    def create_topic(self, topic_name):
        topic = self.pubsub_client.topic(topic_name)

        if not topic.exists():
            topic.create()

        return topic


    def list_topics(self):
        topics = []
        
        for topic in self.pubsub_client.list_topics():
            topics.append(topic.name)

        return topics
    

    def delete_topic(self, topic_name):
        topic = self.pubsub_client.topic(topic_name)

        if topic.exists():
            topic.delete()