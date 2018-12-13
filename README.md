### Access db from terminal
```
docker exec -it djangodocker_db_1 psql -U postgres
```

# How to run
1. docker build . --no-cache
2. run migrations 
```bash
python manage.py migrate
```

# Test
run in container
```bash
python manage.py loaddata stats_fixtures.json
python manage.py loaddata scraper_fixtures.json
pytest
```