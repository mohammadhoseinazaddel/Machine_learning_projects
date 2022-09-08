import json
from time import sleep

from kafka import KafkaConsumer

if __name__ == '__main__':
    parsed_topic_name = 'prepared_videos'
    calories_threshold = 200

    consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    for msg in consumer:
        record = json.loads(msg.value)
        title = record['title']
        date = record['date']
        category = record['category']
        if record['view'] > 2000:
            views = record.get('view')
            print(f'video title {title} with {category} category has {views} publish date {publish_date}')

        sleep(3)
    if consumer is not None:
        consumer.close()
