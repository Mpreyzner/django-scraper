import requests
import json

url = 'http://0.0.0.0:8080/'
timeout = 1


def test_total_stats():
    response = requests.get(url + 'stats/', timeout=1)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(str(exc))
    assert response.status_code == requests.codes.ok
    assert len(response.json()) > 0


def test_author_stats():
    author = 'johndoe'
    response = requests.get(url + 'stats/' + author, timeout=1)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(str(exc))
    assert response.status_code == requests.codes.ok
    assert len(response.json()) > 0


def test_authors():
    response = requests.get(url + 'authors/', timeout=1)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(str(exc))
    assert response.status_code == requests.codes.ok
    assert len(response.json()) > 0
