# FreeMp3Cloud.com Downloader
A lightweight wrapper around FreeMp3Cloud.com to download songs by the given query.

## Installation
```
git clone https://github.com/rtcq/fcloud.git && cd fcloud
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
Seeing the results of the query:
```py
from fcloud import search

songs = search("[TRACK_NAME] [ARTIST_NAME]")
for song in songs:
    print(song.name, song.artist, song.url, song.duration, song.is_high_quality)
```
To download a song:
```py
from fcloud.utils import download_song
download_song(songs[0])
```

## Todo
- [ ] Multithreaded download/search for bulk operations
- [ ] Filter by quality
