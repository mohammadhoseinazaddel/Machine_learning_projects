from time import sleep

import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer


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


def fetch_raw(video_url):
    html = None
    print('Processing..{}'.format(news_url))
    try:
        r = requests.get(video_url, headers=headers)
        if r.status_code == 200:
            html = r.text
    except Exception as ex:
        print('Exception while accessing raw html')
        print(str(ex))
    finally:
        return html.strip()


def get_v3_videos():
    url = 'https://www.varzesh3.com/'
    videos_links = []
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            links = soup.find_all("li", {"class": "video-type"})
            counter = 0
            for link in links:
                video_link = fetch_raw(link.find('a')['href'])
                videos_links.append(video_link)
                counter += 1
                if counter == 20:
                    break
    except Exception as ex:
        #TODO how add kafka logger
        print('Exception in get_v3_videos')
        print(str(ex))
    finally:
        return videos_links


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Pragma': 'no-cache'
    }
    vidoes_link = get_v3_videos()
    if len(vidoes_link) > 0:
        kafka_producer = connect_kafka_producer()
        for link_video in vidoes_link:
            publish_message(kafka_producer, 'raw_videos', 'raw_data', link_video.strip())
        if kafka_producer is not None:
            kafka_producer.close()
