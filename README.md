
### how to start

```
docker-compose build --no-cache
```

```
docker-compose up -d
```

```
docker-compose exec web python manage.py makemigrations <app_name>
eg.) docker-compose exec web python manage.py makemigrations users
eg.) docker-compose exec web python manage.py makemigrations mysite
```

```
docker-compose exec web python manage.py migrate
```

```
docker-compose exec -it web python manage.py createsuperuser
```


### how to refresh all

```
docker container rm -f $(docker container list -aq) && docker volume rm -f $(docker volume list -q) && docker network rm $(docker network list -q)
```
