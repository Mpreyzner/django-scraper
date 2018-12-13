# Django scraper
Small project for blog scraping and calculating word usage statistics for blog post.
Only handles polish.

Doesn't currently handle editing posts.


## Endpoints
There are 3 REST API endpoints.
1. List of blog authors
```bash
curl -v http://0.0.0.0:8080/authors/
```

2. Total blog stats endpoint (returns 10 most used words in all the posts)
```bash
curl -v http://0.0.0.0:8080/stats/
```

3. Author stats endpoint (returns 10 most used worlds in given author posts)
```bash

```
### Access db from terminal
```
docker exec -it djangodocker_db_1 psql -U postgres
```

# How to run
1. docker build . --no-cache
2. docker-compose up
2. run migrations
```bash
docker exec -it djangodocker_web_1 bash # get into container
python manage.py migrate #run migrations in container
```

## Test
run in container
```bash
python manage.py loaddata stats_fixtures.json
python manage.py loaddata scraper_fixtures.json
pytest
```