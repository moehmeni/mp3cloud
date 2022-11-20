# FreeMp3Cloud.com Downloader
A lightweight wrapper around FreeMp3Cloud.com to download songs by the given query.

## Installation
```
git clone https://github.com/nastyrose/fcloud.git && cd fcloud
pip install -r requirements.txt
```

## Usage
### CLI
Downloading a song:
```
python fcloud "[TRACK_NAME] [ARTIST_NAME]"
```
Getting all the URLs provided for the query gathered in a `.txt` file:
```
python fcloud "[TRACK_NAME] [ARTIST_NAME]" --save_urls --no_download
```
### Python programs
```py
from fcloud import search

for song in search("[TRACK_NAME] [ARTIST_NAME]"):
    print(song.name, song.artist, song.url, song.is_high_quality)
```

## Todo
- [ ] Filter by quality
