from typing import List
import requests
from bs4 import BeautifulSoup
import json
import os
from fcloud.objects import Song

url = "https://freemp3cloud.com/downloader"

file_parent_dir = os.path.dirname(os.path.abspath(__file__))
headers_file_path = os.path.join(file_parent_dir, "headers.json")

with open(headers_file_path, "r") as f:
    configs = json.load(f)

session = requests.Session()


def get_initial_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

    r = session.get(url, headers=headers)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def get_token(soup):
    token = soup.find("input", {"name": "__RequestVerificationToken"})["value"]
    return token


def result_soup(q):
    q = q.replace(" ", "+")
    data = {"searchSong": q, "__RequestVerificationToken": configs["token"]}
    headers = configs["headers"]
    r = session.post(url, data, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def search(q) -> List[Song]:
    soup = result_soup(q)
    tags = soup.find_all("div", {"class": "play-item"})
    songs = []
    for tag in tags:
        name = tag.find("div", {"class": "s-title"}).get_text()
        artist = tag.find("div", {"class": "s-artist"}).get_text()
        url = tag.find("div", {"class": "downl"}).find("a")["href"]
        duration = tag.find("div", {"class": "s-time"}).get_text()
        hq = tag.find("div", {"class": "s-hq"}) is not None
        songs.append(Song(
            name=name,
            artist=artist,
            url=url,
            duration=duration,
            hq=hq
        ))
    return songs
