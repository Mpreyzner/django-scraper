import requests

url = 'http://0.0.0.0:8080/'
timeout = 1


def test_total_stats():
    pass


def test_author_stats():
    pass


def test_authors():
    response = requests.get(url + 'authors/', timeout=1)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(str(exc))
    print (response)
    assert 1 == 0
    pass
