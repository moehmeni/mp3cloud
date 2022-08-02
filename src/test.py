import requests
import time
from fcloud import search


def test_results_sustainibility(q):
    i = 1
    songs_count = len(search(q))
    time_pool = []
    while songs_count != 0:
        print(f"Request {i}", end=" - ")
        i += 1
        t1 = time.perf_counter()
        songs_count = len(search(q))
        t2 = time.perf_counter()
        time_pool.append(t2 - t1)
        mean = round(sum(time_pool) / len(time_pool), 4)
        print(f"{songs_count} songs found, Avg time: {mean}", end="\r")


def test_url(url):
    """As long as the url is valid, increase a number and
    show it to the console"""
    i = 1
    while True:
        r = requests.head(url)
        r.raise_for_status()
        print(i, end="\r")
        i += 1


for s in search("bad guy billie eilish"):
    print(s.name, s.artist, s.url)