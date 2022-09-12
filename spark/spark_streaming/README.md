use spark as streaming service with using kafka in it

first you need run kafka

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

