# Eshop

### Demo project with usage of django and kafka

## Project description
- User can log in and logout, his data stored with django session
- User can see users, products and orders pages
- If user logged in he can see orders which belong to him
- Database is postgres
- With each transition to product page, kafka producer sends a message
- Kafka consumer retrieves messages and write them to file every n cycles

## To run 
 ```sh 
pip install -r requirements.txt

# sets up postgres, zookeeper and kafka
sudo docker-compose up -d

python manage.py migrate
python manage.py runserver

# to run kafka consumer
python kafka_consumer.py
```