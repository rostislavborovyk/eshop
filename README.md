# Eshop

### Demo project with usage of django and kafka

## Project description
- User can log in and logout, his data stored with django session
- User can see users, products and orders pages
- If user logged in he can see orders which belong to him
- Database is postgres
- With each transition to product page, kafka producer sends a message with current url
to 'requests' topic, kafka consumer retrieves messages and writes it to redis every
N cycles
- Load tests with cypress 

## To run 
 ```sh 
pip install -r requirements.txt

# sets up postgres, zookeeper, kafka and redis
sudo docker-compose up -d

python manage.py migrate
python manage.py runserver

# to run kafka consumer
python kafka_consumer.py

# to run load tests
bash load_test.sh
```