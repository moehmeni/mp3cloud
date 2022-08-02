from typing import List
import requests
from bs4 import BeautifulSoup
from fcloud.objects import Song

home_url = "https://vww.freemp3cloud.com/"


home_headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9,fa;q=0.8",
    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "__ddgid_=1oM5Id8xmdtHEaYE; __ddg2_=f6iCngi4ZDzNjOC8; __ddg1_=rxcm6FzD6RuNipsDKO9D; .AspNetCore.Antiforgery.2kyQ2nmXF04=CfDJ8NzsyqJ783FKu4o7QZmkp9gQzwa-ZnkL0uMvoFmjo8Mphvmwo7_2fRf1pQeTrTlQb3uSb1vuGX_KjBV90sJVQn2HCWI8wdKlNqLmnUHT7STwrYCbvuSZ_tFvO0lOx3LiPJOPuBGMdcwcbFbLeqZWNKk",
    "Referer": "https://vww.freemp3cloud.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}


search_headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9,fa;q=0.8",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "__ddgid_=1oM5Id8xmdtHEaYE; __ddg2_=f6iCngi4ZDzNjOC8; __ddg1_=rxcm6FzD6RuNipsDKO9D; .AspNetCore.Antiforgery.2kyQ2nmXF04=CfDJ8NzsyqJ783FKu4o7QZmkp9gQzwa-ZnkL0uMvoFmjo8Mphvmwo7_2fRf1pQeTrTlQb3uSb1vuGX_KjBV90sJVQn2HCWI8wdKlNqLmnUHT7STwrYCbvuSZ_tFvO0lOx3LiPJOPuBGMdcwcbFbLeqZWNKk",
    "Referer": "https://vww.freemp3cloud.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}


session = requests.Session()


def soup_of(url, headers):
    r = session.get(url, headers=headers)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def get_token():
    soup = soup_of(home_url, home_headers)
    token = soup.find("input", {"name": "__RequestVerificationToken"})["value"]
    return token


def get_search_soup(q: str):
    q = q.replace(" ", "+")
    data = {"searchSong": q, "__RequestVerificationToken": get_token()}
    r = session.post(home_url, data, headers=search_headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def search(q) -> List[Song]:
    soup = get_search_soup(q)
    tags = soup.find_all("div", {"class": "play-item"})
    for tag in tags:
        name = tag.find("div", {"class": "s-title"}).get_text()
        artist = tag.find("div", {"class": "s-artist"}).get_text()
        url = tag.find("div", {"class": "downl"}).find("a")["href"]
        duration = tag.find("div", {"class": "s-time"}).get_text()
        hq = tag.find("div", {"class": "s-hq"}) is not None
        yield Song(name=name, artist=artist, url=url, duration=duration, hq=hq)