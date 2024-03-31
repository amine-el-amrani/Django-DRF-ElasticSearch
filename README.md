# Django-DRF-ElasticSearch





setup 
create virtual env python3 -m venv env
activate virtual env source env/bin/activate
to create migrations python manage.py makemigrations
to run migrations python manage.py migrate
to run the server python manage.py runserver


to populate the database with some testing data i created a script you can just run the following command python manage.py populate_db If everything went well you should see a Successfully populated the database. message in the console and there should be a few articles in your database.


setup Elasticsearch

docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.11.4
docker run --name elasticsearch --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t docker.elastic.co/elasticsearch/elasticsearch:8.11.4

When you start Elasticsearch for the first time, the generated elastic user password and Kibana enrollment token are output to the terminal. Copy the generated password and enrollment token and save them in a secure location. These values are shown only when you start Elasticsearch for the first time. You’ll use these to enroll Kibana with your Elasticsearch cluster and log in.


Populate Elasticsearch
To create and populate the Elasticsearch index and mapping, use the search_index command:

python manage.py search_index --rebuild

Deleting index 'users'
Deleting index 'categories'
Deleting index 'articles'
Creating index 'users'
Creating index 'categories'
Creating index 'articles'
Indexing 3 'User' objects
Indexing 4 'Article' objects
Indexing 4 'Category' objects
You need to run this command every time you change your index settings.


