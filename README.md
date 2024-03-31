# Simple Blog Application

This project is a simple blog application built with Django and Django REST Framework. It includes multiple models for authors, categories, and articles, which are serialized and served via the Django REST Framework. Additionally, Elasticsearch is integrated to create an endpoint for searching different authors, categories, and articles.

## Project Structure

The project is split into two main apps:

- **blog**: Contains Django models, serializers, and ViewSets for the blog functionality.
- **search**: Handles Elasticsearch documents, indexes, and queries for search functionality.

## Setup

### Virtual Environment

1. Create a virtual environment:
python3 -m venv env

2. Activate the virtual environment:
source env/bin/activate


### Django Setup

1. Create migrations:
python manage.py makemigrations

2. Run migrations:
python manage.py migrate

3. Run the server:
python manage.py runserver


### Populating the Database

To populate the database with some testing data, run the following command:
python manage.py populate_db

If successful, you should see a "Successfully populated the database." message in the console, and there should be a few articles in your database.

### Setting Up Elasticsearch

1. Create a Docker network:
docker network create elastic

2. Pull the Elasticsearch Docker image:
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.11.4

3. Run Elasticsearch:
docker run --name elasticsearch --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t docker.elastic.co/elasticsearch/elasticsearch:8.11.4


**Note**: When you start Elasticsearch for the first time, the generated `elastic` user password and Kibana enrollment token are output to the terminal. Copy these values and save them in a secure location. These values are shown only once and are necessary for enrolling Kibana with your Elasticsearch cluster and logging in.

### Populating Elasticsearch

To create and populate the Elasticsearch index and mapping, use the `search_index` command:
python manage.py search_index --rebuild

This command deletes and recreates the indexes for users, categories, and articles, and indexes the corresponding objects. You need to run this command every time you change your index settings.

## Conclusion

This README provides a brief overview of the Simple Blog Application project, including setup instructions for both Django and Elasticsearch