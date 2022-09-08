# ML2_Exercise

## this project uses kafka as broker and cross platform betwwen two module for crawling
in this example i crawled varzesh3.ir news

![img](statics/images/varzesh%20ah%20ah%203.png)

#### to use it do below

clone dockerkafka project:
https://github.com/wurstmeister/kafka-docker

```bash
cd {in_cloned_repo}
```

install kafka  with docker-compose 

```bash
sudo docker-compose up -d
```

 now kafka is listening on port 9092

![img](statics/images/docker-compose%20up.png)

now run producer_of_raw_data.py 

```python
python producer_of_raw_data.py
```
in this level you craled all video news link and jump to it and the results sent to topic of kafka that named **raw_videos** with **raw_data** key name

then you want to find out the title catgory and data and *view* of that new so run

```python
python producer_consumer_videos_midlewre.py
```
now the prepared data are in **prepared_videos** kafka topic

now the last part is show the data if they have mor than 2k views eith below output consule format

'video title {title} with {category} category has {views} publish date {publish_date}'

guaidance:
https://github.com/wurstmeister/kafka-docker

example:

https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05

https://github.com/kadnan/Calories-Alert-Kafka
