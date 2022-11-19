class Song:
    def __init__(self, name, artist, url, duration=0, is_high_quality=False):
        self.name = name
        self.artist = artist
        self.url = url
        self.duration = duration
        self.is_high_quality = is_high_quality

    def __str__(self) -> str:
        return f"{self.name} - {self.artist}"
