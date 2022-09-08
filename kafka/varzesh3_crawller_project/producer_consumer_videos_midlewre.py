import json
from time import sleep
import re

from bs4 import BeautifulSoup
from kafka import KafkaConsumer, KafkaProducer


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


def parse(markup):
    wanted_attr_dict = {}
    k = False

    try:

        soup = BeautifulSoup(markup, 'lxml')
        category = soup.find("a", {"class": "category"})
        title = soup.find("div", {"class": ["video-title"]}).find('h1')
        date = soup.find("span", {"class": ["date"]})
        views_section = soup.find("span", {"class": ["view"]}).text
        view = re.findall(r"([\d.]*\d+)", first_part := views_section.split()[0])
        
        if "k" in first_part:
            veiw_count = int(view[0])*1000
        else:
            veiw_count = int(view[0])    
            
            wanted_attr_dict = {
                'title': title.text,
                'category': category.text
                'date': date.text,
                'view': veiw_count,
            }

    except Exception as ex:
        print(title_section)
        print('Exception while parsing')
        print(str(ex))
    finally:
        return json.dumps(wanted_attr_dict)


if __name__ == '__main__':
    print('Running Consumer..')
    parsed_records = []
    topic_name = 'raw_videos'
    parsed_topic_name = 'prepared_videos'

    consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    for msg in consumer:
        html = msg.value
        result = parse(html)
        parsed_records.append(result)

    consumer.close()
    sleep(5)

    if len(parsed_records) > 0:
        print('Publishing records..')
        producer = connect_kafka_producer()
        for wanted_attr_dict in parsed_records:
            publish_message(producer, parsed_topic_name, 'prepared_data', wanted_attr_dict)
