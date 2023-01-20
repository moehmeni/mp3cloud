# FreeMp3Cloud Downloader
[![Downloads](https://pepy.tech/badge/mp3cloud)](https://pepy.tech/project/mp3cloud)

A lightweight wrapper around [FreeMp3Cloud.com](https://freemp3cloud.com) to download songs by the given query.

## Installation
```
pip install mp3cloud
```
**Note `cURL` should be installed**

## Usage
### CLI
Downloading a song:
```
python -m mp3cloud "[TRACK_NAME] [ARTIST_NAME]"
```
Getting all the URLs provided for the query gathered in a `.txt` file:
```
python -m mp3cloud "[TRACK_NAME] [ARTIST_NAME]" --save-urls --no-download
```
### Python programs
Seeing the results of the query:
```py
from mp3cloud import search

songs = search("[TRACK_NAME] [ARTIST_NAME]")
for song in songs:
    print(song.name, song.artist, song.url, song.duration, song.is_high_quality)
```
To download a song:
```py
from mp3cloud.utils import download_song
download_song(songs[0])
```

## Todo
- [ ] Setting metadata for the downloaded song
- [ ] Filter by quality
- [ ] Checking the availablity of cURL
- [ ] Add docs for the functions
