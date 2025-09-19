from abc import ABC, abstractmethod

# --- Iterator Interface ---
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass

# --- Aggregate / Collection ---
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song: str):
        self.songs.append(song)

    def create_iterator(self):
        return PlaylistIterator(self.songs)

# --- Concrete Iterator ---
class PlaylistIterator(Iterator):
    def __init__(self, songs):
        self._songs = songs
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._songs)

    def next(self):
        if self.has_next():
            song = self._songs[self._index]
            self._index += 1
            return song
        else:
            raise StopIteration

# --- Client Code ---
if __name__ == "__main__":
    playlist = Playlist()
    playlist.add_song("Song A")
    playlist.add_song("Song B")
    playlist.add_song("Song C")

    iterator = playlist.create_iterator()

    while iterator.has_next():
        song = iterator.next()
        print("Playing:", song)
