#HackDay Donate


##Install

1.Install Deps

    pip install -r requirements.txt

2.Install ElasticSearch

	brew install elasticsearch
	brew install postgresql
	brew install postgis
	brew install gdal
	brew install libgeoip

3.Create Database

    python manage.py syncdb

4.Create ``local_settings.py``

```python
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "I do not know"
NEVERCACHE_KEY = "I do not know"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'django',
    },
}
```

5.Run
 
	python manage.py runserver    

##Tech

- ElasticSearch
- Django
- Ionic
- OpenLayers 3

##Document

[Mac OS Django Geo 环境搭建](http://www.phodal.com/blog/django-elasticsearch-geo-solution/)

[AWS CentOS Django Geo 环境搭建](http://www.phodal.com/blog/install-geo-django-in-centos/)
