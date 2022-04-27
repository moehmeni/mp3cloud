class Song:
    def __init__(self, name, artist, url, duration=0, hq=False):
        self.name = name
        self.artist = artist
        self.url = url
        self.duration = duration
        self.hq = hq

    def __str__(self) -> str:
        return f"{self.name} - {self.artist}"
