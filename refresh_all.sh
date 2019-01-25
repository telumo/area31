
# 全てのコンテナとボリュームとネットワークを削除
docker container rm -f $(docker container list -aq) && docker volume rm -f $(docker volume list -q) && docker network rm $(docker network list -q)

rm -rf ./src/*/__pycache__ && rm -rf ./src/*/migrations 

docker-compose build --no-cache
docker-compose up -d

docker-compose exec web python manage.py makemigrations
# 失敗する場合は、docker exec -it mysite.web bash から実行
docker-compose exec web python manage.py migrate

docker-compose exec -it web python manage.py createsuperuser
