import requests
import time
from mp3cloud import search


def test_results_sustainibility(q):
    """Checks how sustainable a search result is.
    It prints out average request time and songs count for each test"""
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
        print(f"{songs_count} songs found, Avg time for each request: {mean}", end="\r")


def test_url(url):
    """As long as the song url is valid, increases a number and
    shows it to the console"""
    i = 1
    while True:
        r = requests.head(url)
        r.raise_for_status()
        print(i, end="\r")
        i += 1


def test_results_for(q: str):
    """Shows the results for given query"""
    for s in search(q):
        print(s.name, s.artist, s.url)


if __name__ == "__main__":
    q = "Billie eilish bad guy"
    # test_results_sustainibility(q)
    test_results_for(q)
